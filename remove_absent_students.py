"""Remove missing students from group assignment"""
#from random import shuffle
#import itertools
#import argparse
#import sys
#function files

def remove_absent_students(absentee_list, list_of_student_lists):
    """Remove missing students before group assignment"""
    list_of_student_lists_copy = list_of_student_lists[:]
    for name in absentee_list:
        for student_list in list_of_student_lists:
            if student_list[0] == name:
                list_of_student_lists_copy.remove(student_list)
    return list_of_student_lists_copy
