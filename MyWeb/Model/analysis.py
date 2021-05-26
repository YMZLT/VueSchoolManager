import pandas as pd
import sqlalchemy


class Analysis():
    def __init__(self) -> None:
        # 连接 Mysql 数据库:
        # engine = sqlalchemy.create_engine('mysql+pymysql://root:root@localhost:3306/express')
        # 连接 sqlite 数据库:
        # sqlite://<nohostname>/<path>
        # where <path> is relative:
        self.engine = sqlalchemy.create_engine("sqlite:///db.sqlite3")
    def getBasicData(self,semester):
        # 计算每学期每个开课课程的难度系数、及格人数、及格率、平均分、最高分、最低分
        query = '''
        SELECT C.*,O.semester,O.teacher_id,U.user_name,O.course_time,
        COUNT(student_id) as student_num,
        SUM(case when score>=60 then 1 else 0 end) as pass_num,
        MAX(score) as score_max,MIN(score) as score_min,
        AVG(score) as score_avg
        from OpenTable as O,ScoreTable as S,Coursetable as C,User as U
        where S.open_id=O.id and C.course_id=O.course_id and U.user_id=O.teacher_id and semester={0}
        group by O.course_id
        '''.format(semester)
        pass_num_table = pd.read_sql_query(query, self.engine)
        pass_num_table["pass_rate"]=pass_num_table[["pass_num","student_num"]].apply(lambda x:x["pass_num"]/x["student_num"],axis=1)
        # pass_num_table["pass_rate"] = pass_num_table["pass_rate"].apply(lambda x:format(x,'.2%'))
        pass_num_table["difficulty"]=pass_num_table[["score_avg"]].apply(lambda x:1-x["score_avg"]/100,axis=1)
        pass_num_table = pass_num_table.round(2)
        pass_num_table_dict = pass_num_table.to_dict(orient='records')
        return pass_num_table_dict
    def getScoreDistribution(self,semester):
        # 计算每学期每个开课课程的成绩分布情况
        query = '''
        SELECT course_id,
        SUM(case when score>=90 and score<=100 then 1 else 0 end) as class_A,
        SUM(case when score>=80 and score<90 then 1 else 0 end) as class_B,
        SUM(case when score>=70 and score<80 then 1 else 0 end) as class_C,
        SUM(case when score>=60 and score<70 then 1 else 0 end) as class_D,
        SUM(case when score>=0 and score<60 then 1 else 0 end) as class_E
        from OpenTable as O,ScoreTable as S
        where S.open_id=O.id and semester={0}
        group by course_id
        '''.format(semester)
        score_distribution = pd.read_sql_query(query, self.engine)
        score_distribution_dict = score_distribution.to_dict(orient='split')
        return score_distribution_dict

    def getAvgScore(self,student_id):
        # 学生平均成绩变化
        query = '''
                SELECT O.semester,AVG(score) as avg_score
                FROM ScoreTable as S,OpenTable as O
                where student_id = {0} and O.id = S.open_id
                group by O.semester
                '''.format(student_id)
        Avg_table = pd.read_sql_query(query, self.engine)
        return Avg_table.round(2)




