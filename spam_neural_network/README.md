# Spam Neural Network

This project was created for an assignment in my Programming II class. The assignment required the creation and training of a boolean neural network using a simple dataset.

For my project, I decided to create a neural network that could read the subject line of an email, and guess whether or not the email was "Spam" or "Ham."

"Spam" refers to unsolicited and often irrelevant or inappropriate messages sent over the internet to a large number of recipients while "Ham" refers to legitimate, non-spam emails that are desired and expected by the recipient.

The Neural Network was trained on a dataset of negative keywords and phrases that are common in spam emails.

After the training, the network was tested on a dataset of email subject lines, with some being Spam and some being Ham. After the neural network labelled each email as Spam or Ham, the list of neural network guesses was tested against the list of correct email assessments.

Following the testing process, a percentage score was printed in the console, giving a direct numerical value of accuracy. 

After running the neural network 10 times, the average accuracy of its Spam assessment was 98.52%.

*Running this code requires the installation of the Scikit-Learn and Pandas libraries

