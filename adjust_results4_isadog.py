 
def adjust_results4_isadog(results_dic, dogfile):
    """
    Adjusts the results dictionary to determine if classifier correctly 
    classified images 'as a dog' or 'not a dog' especially when not a match. 
    Demonstrates if model architecture correctly classifies dog images even if
    it gets dog breed wrong (not a match).
    Parameters:
      results_dic - Dictionary with 'key' as image filename and 'value' as a 
                    List. Where the list will contain the following items: 
                  index 0 = pet image label (string)
                  index 1 = classifier label (string)
                  index 2 = 1/0 (int)  where 1 = match between pet image
                    and classifer labels and 0 = no match between labels
                ------ where index 3 & index 4 are added by this function -----
                 NEW - index 3 = 1/0 (int)  where 1 = pet image 'is-a' dog and 
                            0 = pet Image 'is-NOT-a' dog. 
                 NEW - index 4 = 1/0 (int)  where 1 = Classifier classifies image 
                            'as-a' dog and 0 = Classifier classifies image  
                            'as-NOT-a' dog.
     dogfile - A text file that contains names of all dogs from the classifier
               function and dog names from the pet image files. This file has 
               one dog name per line dog names are all in lowercase with 
               spaces separating the distinct words of the dog name. Dog names
               from the classifier function can be a string of dog names separated
               by commas when a particular breed of dog has multiple dog names 
               associated with that breed (ex. maltese dog, maltese terrier, 
               maltese) (string - indicates text file's filename)
    Returns:
           None - results_dic is mutable data type so no return needed.
    """           
    with open(dogfile, 'r') as f:
        dognames_set = {name.strip() for name in f if name.strip()}
        # strip() removes the leading and trailing whitsapces as well as newline '\n' 
        # if there is empty line in text file then strip will give '' which is considered False
        # By making set, we also encounter the duplicate namees
    
    # For O(1) searching, lets store dognames in dictionary
    dognames_dict = {name: 1 for name in dognames_set}
    
    for filename in results_dic:
        true_label = results_dic[filename][0]
        classifier_label = results_dic[filename][1]
        
        results_dic[filename].append(1 if true_label in dognames_dict else 0)
        results_dic[filename].append(1 if classifier_label in dognames_dict else 0)

        
        
