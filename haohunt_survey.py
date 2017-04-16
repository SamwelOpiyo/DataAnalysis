import requests
import json
import pandas as pd
class AnswerAnalysis(object):
    def __init__(self):
        self.load = requests.get("https://samwelopiyo.herokuapp.com/haohunt/all").text
        self.json_conversion = json.loads(self.load)
        self.answer_list = [self.json_conversion["responses"][i]["answers"] for i in range(len(self.json_conversion["responses"])) if self.json_conversion["responses"][i]["answers"]]
        self.frame = pd.DataFrame(self.answer_list)
        print "Emails Collected:"
        print self.email_analysis()
        print "\n\n"
        print "Are you a student at a university or a college?"
        print self.student_analysis()
        print "\n\n"
        print "Which University are you currently enrolled in?"
        print self.university_analysis()
        print "\n\n"
        print "How far is your place of Accommodation from your college/university?"
        print self.distance_analysis()
        print "\n\n"
        print "How many people do you stay with in your place of accommodation?"
        print self.roommates_analysis()
        print "\n\n"
        print "How much do you spend per semester on accommodation?"
        print self.fees_analysis()
        print "\n\n"
        print "What major problems have you encountered while looking for accommodation or while staying in your place of accommodation?"
        print self.user_problems()
        print "\n\n"

    def email_analysis(self):
        self.email_count = self.frame["email_47420161"].value_counts()
        return self.email_count 
    def student_analysis(self):
        self.student_count = self.frame["yesno_47409758"].value_counts()
        return self.student_count 
    def university_analysis(self):
        self. university_count = self.frame["dropdown_47416838"].value_counts()
        return self.university_count 
    def distance_analysis(self):
        self.distance_from_university_count = self.frame["list_47417778_choice"].value_counts()
        return self.distance_from_university_count 
    def roommates_analysis(self):
        self.people_stay_with_count = self.frame["list_47418134_choice"].value_counts()
        return self.people_stay_with_count 
    def fees_analysis(self):
        self.accommodation_fees_persem_count = self.frame["list_47418512_choice"].value_counts()
        return self.accommodation_fees_persem_count
    def user_problems(self):
        self.problems_byuser_count = self.frame["textfield_47419084"].value_counts()
        return self.problems_byuser_count 
"""
    problems_ease_of_booking_count = frame["list_47419192_choice_60077092"].value_counts()
    problems_long_queues_count = frame["list_47419192_choice_60077093"].value_counts()
    problems_late_bookings_count = frame["list_47419192_choice_60077094"].value_counts()
    problems_poor_services_count = frame["list_47419192_choice_60077095"].value_counts()
    problems_uncondusive_environment_count = frame["list_47419192_choice_60077096"].value_counts()
    problems_poor_customer_service = frame["list_47419192_choice_60078445"].value_counts()
    description_good_place_of_accommodation_count = frame["textfield_47419458"].value_counts()
    willing_to_pay_count = frame["number_47419688"].value_counts()
    willing_to_pay_average = frame["number_47419688"].mean()
    return email_count,
            student_count,
            university_count,
            distance_from_university_count,
            people_stay_with_count,
            accommodation_fees_persem_count,
            problems_byuser_count,
            problems_ease_of_booking_count,
            problems_long_queues_count,
            problems_late_bookings_count,
            problems_poor_services_count,
            problems_uncondusive_environment_count,
            problems_poor_customer_service,
            description_good_place_of_accommodation_count,
            willing_to_pay_count,
            willing_to_pay_average

print answer_analysis()
"""
