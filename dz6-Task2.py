#Написать такое lamda выражение transformation, чтобы transfored_values получился копией values 

transformations=(lambda i: i)
values=[2,3,5,7,11,13,17,19,23,'gdgd']
transformed_values=list(map(transformations,values))
