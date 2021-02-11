def are_anagrams(s1, s2, s3):
    """
    we convert function arguments into the list, as it would be easier
	to deal with it later on, as every argument needs to be the subject
	of the same actions
    """
    arr = [s1, s2, s3]
    """
    we check if the length of all arguments doesn't exceed the provided
	limit of 5 characters
    """
    if not all(len(item)<= 5 for item in arr):
        return("Sorry, all \"are_anagrams\" function arguments shall be "\
		"at most 5 characters long.")
    """
    first, we unify the formating of input data by lowering the case,
	next we convert every string into the list of characters, which is
	then sorted in alphabetical order to allow the verification if every
	string consists of the same characters
    """
    arr = [sorted(list(x.lower())) for x in arr]
    """
    first idea was to just compare every element of the list
	(arr[0]==arr[1]==arr[2]), but to make the code scalable we compare
	if the first element of the list appears the same number of times as
	the number of all list elements
    """
    return(arr.count(arr[0])==len(arr))