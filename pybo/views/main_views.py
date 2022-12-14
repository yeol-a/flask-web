from flask import Blueprint, url_for
from werkzeug.utils import redirect


bp = Blueprint('main', __name__, url_prefix='/')


@bp.route('/hello')
def hello_pybo():
    return 'I am Hailey'


@bp.route('/')
def index():
    return redirect(url_for('question._list'))
    #return render_template(~~.html)


# @bp.route('/')
# def index():
#     question_list=Question.query.order_by(Question.create_date.desc())
#     return render_template('question/question_list.html', question_list=question_list)


# @bp.route('/detail/<int:question_id>/')
# def detail(question_id):
#     question = Question.query.get_or_404(question_id)
#     return render_template('question/question_detail.html', question=question)