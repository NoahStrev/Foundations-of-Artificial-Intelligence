# Some courses may have prerequisites
# given the total number of courses and a list of prerequisite pairs
# we have to find the ordering of courses that we should take to finish all courses.
# There may be multiple correct orders, we just need to find one of them.
# Two electives were added to the list of required courses as well.

graph = {
  'CSC351' : ['CSC111'],
  'Elec:440': ['CSC341'],
  'CSC110' : [ ],
  'Elec:353': ['CSC110'],
  'CSC450' : ['CSC226', 'CSC110', 'CSC111', 'CSC240', 'CSC341', 'CSC351'] ,
  'CSC111' : ['CSC110'],
  'CSC341' : ['CSC226'],
  'CSC226' : ['CSC111'],
  'CSC240' : [ ],
  'CSC480' : ['CSC341'],
  'Complete Major' : ['CSC450', 'Elec:353', 'Elec:440','CSC480']
}
