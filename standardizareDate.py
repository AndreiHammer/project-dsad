import pandas as pd


educatie_df = pd.read_csv("data_raw/cadredidactice_neformatat.csv")
educatie_df.columns = educatie_df.columns.str.strip()

regiuni_df = pd.read_csv("data_raw/Teritorial_2022.csv")
regiuni_df.columns = regiuni_df.columns.str.strip()


educatie_df = educatie_df.rename(columns={
    "Niveluri de educatie": "Nivel educatie",
    "Macroregiuni  regiuni de dezvoltare si judete": "Judet",
    "Valoare": "Valoare"
})
educatie_df["Judet"] = educatie_df["Judet"].str.strip().str.lower()

regiuni_df = regiuni_df.rename(columns={
    "Judet": "Judet",
    "Regiunea": "Regiune",
    "Macroregiunea": "Macroregiune"
})
regiuni_df["Judet"] = regiuni_df["Judet"].str.strip().str.lower()


educatie_df = educatie_df[["Nivel educatie", "Judet", "Valoare"]]
educatie_pivot = educatie_df.pivot_table(
    index="Judet",
    columns="Nivel educatie",
    values="Valoare",
    aggfunc="sum"
).reset_index()

niveluri_educatie = [
    "In invatamantul anteprescolar", "In invatamantul prescolar",
    "In invatamantul primar", "In invatamantul gimnazial secundar ciclul 1",
    "In invatamantul liceal", "In scoli profesionale - invatamant dual",
    "In invatamantul postliceal si de maistri", "In invatamantul universitar"
]

for nivel in niveluri_educatie:
    if nivel not in educatie_pivot.columns:
        educatie_pivot[nivel] = 0

regiuni_df = regiuni_df[["Indicativ", "Judet", "Regiune", "Macroregiune"]]

final_df = pd.merge(regiuni_df, educatie_pivot, on="Judet", how="left")

final_df = final_df.fillna(0)

final_df = final_df.rename(columns={
    "In invatamantul anteprescolar":"Invatamant anteprescolar",
    "In invatamantul gimnazial secundar ciclul 1":"Invatamant gimnazial",
    "In invatamantul liceal":"Invatamant liceal",
    "In invatamantul postliceal si de maistri":"Invatamant postliceal si de maistri",
    "In invatamantul prescolar":"Invatamant prescolar",
    "In invatamantul primar":"Invatamant primar",
    "In invatamantul universitar":"Invatamant universitar",
    "In scoli profesionale - invatamant dual":"Invatamant profesional",
})

output_file = "data_in/personal_didactic_2023.csv"
final_df.to_csv(output_file, index=False, float_format="%.0f")

print(f"Fisierul final a fost salvat ca: {output_file}")


