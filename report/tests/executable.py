from report.survey_gen import Choices
from report.survey_gen import HtmlSurvey

htmlsurvey = HtmlSurvey()
answer = htmlsurvey.get()
surveyresult = Choices(answer=answer)
print_result: str = surveyresult.get_result_text()
print(print_result)
