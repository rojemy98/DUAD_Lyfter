class Student:
    """
    Represents a student entity.
    This class only defines the data structure (no business logic).
    """

    def __init__(self, name, section, spanish, english, social, science):
        # Basic information
        self.name = name
        self.section = section

        # Academic grades
        self.spanish_grade = spanish
        self.english_grade = english
        self.social_studies_grade = social
        self.science_grade = science