# AuctionWebApp
This has been created to fulfil the needs of the group coursework for ECS639U. The group consists of Lana Allingham, Nathan Johnson, Dilani Selvanathan and Nicholas Sheward.

Below is the description that was given:

"Your task is to develop an auction website (think of Ebay) using the Django framework. The website should provide the following functionalities:
1. Users can create an account on the site and and able to login into their account.
2. The user’s proLile should contain at least an email and their date of birth.
3. Users should be able to post a new item for auction. Items should contain a title, a
description, a picture and the date/time the auction Linishes.
4. Users of the site should then be able to bid for an item, before the end date/time of
that item.
5. At the end of the auction, the highest bidder is able to “buy” the item. You do not need
to implement the “payment” process, but your app should alert the winner, e.g. via a
message page or as part of their proLile.
6. The site must contain a page listing all the items that are currently available, with the
ability for “search” for items based on a given keyword. For instance, searching for “table” should return the list of items that have “table” as part of the title or the description. The searching mechanism should be done using ajax (so no page refreshes).
7. You should also have a page containing “closed” auctions, detailing the list of biddings, and the winner.
8. The frontend should use Bootstrap, and be responsive.
9. For top marks, apart from the basic features above, your group should implement at
least one extra feature. Feel free to include any extra feature you can think of. Here are three examples of possible extra features:

  a) At the end of the auction, the winner receives an email conLirming that they should proceed to purchase the item. You might need to use a cron job, so you regularly check for “closed” auctions.

  b) Users are able to send questions to the item owner about the condition of the item, and the owner is able to reply to those questions.

  c) Users are able to reset their password, in case they have forgotten it. This would be done via a “reset password link” sent to their email.

Emails: If you app is sending emails, please create temporary Gmail account, and use that to send emails, as you will need to submit the code for your app which might contain the password for the email account (unless you are using environment variables on the server to store your passwords).

Outcome: Once fully tested, your application should be deployed to the school’s OpenShift web servers (to be discussed in week 7) — one deployed app per team. Each group should submit the code together with a one-page report describing their extra feature (no more than a few paragraphs). Submit these to QM+ as a single zip Lile. Remember to include in the report the URL of your deployed application, and the username and password for the admin page.""

A Google account was created for the purpose of this coursework. The details are below:

Username: ECS639UGroup2@gmail.com

Password: Group2Coursework

There is nothing of  importance in the above account and so no efforts were made to keep it secure.

requirements.txt file can be used to easily install the required packages. To take advantage of this, please run:

``pip install -r auctionsite/requirements.txt``
