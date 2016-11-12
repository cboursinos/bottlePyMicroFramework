
from application import template_filter, trans_db
from bottle import request


@template_filter
def trans_do(text):
    print text
    if request.get_cookie("lang"):
        lang = request.get_cookie("lang")
    else:
        lang = 'en-US'
    if text not in trans_db:
        return ''
    translate = trans_db[text][lang]
    if translate:
        return translate
    else:
        return text

