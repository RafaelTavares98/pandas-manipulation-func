import azure.functions as func
import pandas as pd
import io
import json
import logging

app = func.FunctionApp()

@app.route(route="PandasManipulationFunc", auth_level=func.AuthLevel.ANONYMOUS)
def PandasManipulationFunc(req: func.HttpRequest) -> func.HttpResponse:
    try:
        raw_body = req.get_body()
        logging.info(f"Raw request body: {raw_body.decode('utf-8', errors='ignore')}")
        data = req.get_json()
    except Exception as e:
        logging.exception("Erro ao interpretar JSON:")
        return func.HttpResponse(f"Erro ao ler JSON: {e}", status_code=400)

    if not isinstance(data, dict):
        logging.warning(f"Formato inesperado: {type(data)}")
        return func.HttpResponse("Corpo da requisição não é um JSON objeto.", status_code=422)

    if "students" not in data:
        logging.warning("Campo 'students' ausente.")
        return func.HttpResponse("Campo 'students' ausente no JSON.", status_code=422)

    logging.info(f"JSON recebido com {len(data['students'])} estudantes.")

    df = pd.DataFrame(data["students"])
    df_exploded = df.explode("courses").reset_index(drop=True)
    courses_norm = pd.json_normalize(df_exploded["courses"])
    merged = pd.concat([df_exploded.drop(columns=["courses"]), courses_norm], axis=1)

    csv_buf = io.StringIO()
    merged.to_csv(csv_buf, index=False)

    logging.info("Transformação concluída com sucesso.")
    return func.HttpResponse(csv_buf.getvalue(), mimetype="text/csv")
