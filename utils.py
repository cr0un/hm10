import json

def get_canditates(path):
    with open ('../candidates.json', 'r', encoding='utf-8') as candidates:
        return json.load(candidates)

def format_candidates(candidates_list):
    result = '<pre>'
    for candidate in candidates_list:
        result += (
f'Имя кандидата - {candidate["name"]}\n'
f'Позиция кандидата - {candidate["position"]}\n'
f'Навыки через запятую - {candidate["skills"]}\n\n'
        )
    result += '<pre>'
    return result

def get_candidate_by_id(candidates_list, candidates_id):
    for candidate in candidates_list:
        if candidate['id'] == candidates_id:
            return candidate

def get_candidates_by_skill(candidates_list, candidates_skill):
    result = []
    for candidate in candidates_list:
        candidates_skills = candidate['skills'].lower().split(', ')
        if candidates_skill.lower() in candidates_skills:
            result.append(candidate)
    return result

