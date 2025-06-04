import json
import argparse


def interpret_bmi(bmi: float) -> str:
    if bmi < 18.5:
        return "저체중"
    elif bmi < 23:
        return "정상체중"
    elif bmi < 25:
        return "과체중"
    else:
        return "비만"


def interpret_bp(sbp: int, dbp: int) -> str:
    if sbp < 120 and dbp < 80:
        return "정상 혈압"
    elif sbp < 130 and dbp < 80:
        return "정상 이상"
    elif sbp < 140 or dbp < 90:
        return "고혈압 전단계"
    else:
        return "고혈압"


def interpret_ldl(ldl: float) -> str:
    if ldl < 100:
        return "정상 LDL"
    elif ldl < 130:
        return "경계 LDL"
    else:
        return "높은 LDL"


def generate_doctor_note(data: dict) -> str:
    notes = []

    bmi_status = interpret_bmi(data.get("bmi", 0))
    notes.append(f"BMI {data.get('bmi')}로 {bmi_status}입니다.")

    sbp = data.get("sbp", 0)
    dbp = data.get("dbp", 0)
    bp_status = interpret_bp(sbp, dbp)
    notes.append(f"혈압 {sbp}/{dbp} mmHg로 {bp_status}입니다.")

    fasting = data.get("fasting_glucose", 0)
    if fasting < 100:
        g_status = "정상"
    elif fasting < 126:
        g_status = "공복혈당장애"
    else:
        g_status = "당뇨병 의심"
    notes.append(f"공복 혈당 {fasting} mg/dL로 {g_status}입니다.")

    ldl = data.get("ldl", 0)
    chol_status = interpret_ldl(ldl)
    notes.append(f"LDL 콜레스테롤 {ldl} mg/dL로 {chol_status}입니다.")

    ast = data.get("ast")
    alt = data.get("alt")
    if ast is not None and alt is not None:
        if ast > 40 or alt > 40:
            notes.append(f"간효소 수치(AST {ast}, ALT {alt})가 높아 간기능 이상이 의심됩니다.")
        else:
            notes.append(f"간효소 수치(AST {ast}, ALT {alt})가 정상 범위입니다.")

    creatinine = data.get("creatinine")
    if creatinine is not None:
        if creatinine > 1.2:
            notes.append(f"혈청 크레아티닌 {creatinine} mg/dL로 신장 기능 저하가 우려됩니다.")
        else:
            notes.append(f"혈청 크레아티닌 {creatinine} mg/dL로 신장 기능은 정상입니다.")

    return "\n".join(notes)


if __name__ == "__main__":
    parser = argparse.ArgumentParser(description="건강검진 결과로 의사 소견을 생성합니다.")
    parser.add_argument("json_file", help="검진 결과가 들어있는 JSON 파일 경로")
    args = parser.parse_args()

    with open(args.json_file, "r", encoding="utf-8") as f:
        data = json.load(f)

    note = generate_doctor_note(data)
    print(note)
