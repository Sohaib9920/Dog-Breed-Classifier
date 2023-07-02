 
def calculates_results_stats(results_dic):
        """
        Calculates statistics of the results of the program run using classifier's model 
        architecture to classifying pet images. Then puts the results statistics in a 
        dictionary (results_stats_dic) so that it's returned for printing as to help
        the user to determine the 'best' model for classifying images. Note that 
        the statistics calculated as the results are either percentages or counts.
        Parameters:
        results_dic - Dictionary with key as image filename and value as a List 
                (index)idx 0 = pet image label (string)
                        idx 1 = classifier label (string)
                        idx 2 = 1/0 (int)  where 1 = match between pet image and 
                                classifer labels and 0 = no match between labels
                        idx 3 = 1/0 (int)  where 1 = pet image 'is-a' dog and 
                                0 = pet Image 'is-NOT-a' dog. 
                        idx 4 = 1/0 (int)  where 1 = Classifier classifies image 
                                'as-a' dog and 0 = Classifier classifies image  
                                'as-NOT-a' dog.
        Returns:
        results_stats_dic - Dictionary that contains the results statistics (either
                        a percentage or a count) where the key is the statistic's 
                        name (starting with 'pct' for percentage or 'n' for count)
                        and the value is the statistic's value. See comments above
                        and the previous topic Calculating Results in the class for details
                        on how to calculate the counts and statistics.
        """        

        n_dogs_img, n_notdogs_img, n_match, n_correct_dogs, n_correct_notdogs, n_correct_breed = 0, 0, 0, 0, 0, 0

        for filename in results_dic:

                results = results_dic[filename]

                if results[3] == 1:
                        n_dogs_img += 1

                if results[3] == 0:
                        n_notdogs_img += 1

                if results[3] == 1 and results[4] == 1:
                        n_correct_dogs += 1

                if results[3] == 0 and results[4] == 0:
                        n_correct_notdogs += 1

                if results[2] == 1:
                        n_match += 1
                
                if results[3] == 1 and results[2] == 1:
                        n_correct_breed += 1
                
        n_images = len(results_dic)
        pct_match = 100 * n_match / n_images
        pct_correct_dogs = 100 * n_correct_dogs / n_dogs_img
        pct_correct_notdogs = 100 * n_correct_notdogs / n_notdogs_img
        pct_correct_breed = 100 * n_correct_breed / n_dogs_img

        return {'n_images':n_images, 
                'n_dogs_img': n_dogs_img, 
                'n_notdogs_img': n_notdogs_img, 
                'n_correct_dogs': n_correct_dogs,
                'n_correct_notdogs': n_correct_notdogs,
                'n_correct_breed': n_correct_breed,
                'n_match': n_match,
                'pct_match': pct_match,
                'pct_correct_dogs': pct_correct_dogs,
                'pct_correct_notdogs': pct_correct_notdogs,
                'pct_correct_breed': pct_correct_breed
                }

                

                
