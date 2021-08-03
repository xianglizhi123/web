class Applicant(object):
    def __init__(self,id,apply_date,issue_date,from_school,to_school,apply_location,citizenship,province,major,nick_name):
        self.apply_date = apply_date
        self.from_school = from_school
        self.to_school = to_school
        self.apply_location = apply_location
        self.citizenship = citizenship
        self.province = province
        self.major = major
        self.issue_date = issue_date
        self.id = id
        self.nick_name = nick_name
