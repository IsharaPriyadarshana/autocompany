 .----------------.  .----------------.  .----------------.  .----------------.  .----------------.  .----------------. 
| .--------------. || .--------------. || .--------------. || .--------------. || .--------------. || .--------------. |
| |  _______     | || |  _________   | || |      __      | || |  ________    | || | ____    ____ | || |  _________   | |
| | |_   __ \    | || | |_   ___  |  | || |     /  \     | || | |_   ___ `.  | || ||_   \  /   _|| || | |_   ___  |  | |
| |   | |__) |   | || |   | |_  \_|  | || |    / /\ \    | || |   | |   `. \ | || |  |   \/   |  | || |   | |_  \_|  | |
| |   |  __ /    | || |   |  _|  _   | || |   / ____ \   | || |   | |    | | | || |  | |\  /| |  | || |   |  _|  _   | |
| |  _| |  \ \_  | || |  _| |___/ |  | || | _/ /    \ \_ | || |  _| |___.' / | || | _| |_\/_| |_ | || |  _| |___/ |  | |
| | |____| |___| | || | |_________|  | || ||____|  |____|| || | |________.'  | || ||_____||_____|| || | |_________|  | |
| |              | || |              | || |              | || |              | || |              | || |              | |
| '--------------' || '--------------' || '--------------' || '--------------' || '--------------' || '--------------' |
 '----------------'  '----------------'  '----------------'  '----------------'  '----------------'  '----------------' 
 
 Please follow the below instructions to setup the environment to run the Django app (In Windows)
 
 1. Extract the autocompany.zip file
 2. Create a PostgresDB named 'autocompany' in pgAdmin
 3. Use the autocompany.sql file to restore the DB (select the newly created autocompany db and select restore)
 4. open autocompany/settings.py file and change the DATABASE configurations appropriately with your HOsT, USER and PASSWORD. 
		Eg: 
			DATABASES = {
				'default': {
					'ENGINE': 'django.db.backends.postgresql',
					'NAME': 'autocompany',
					'USER': 'postgres',
					'PASSWORD': '1234',
					'HOST': 'localhost'
				}
			}	


			
 4. Open Command Prompt in autocompany directory
 5. You should have python 3.x installed or else please installed
	+ pip install python
	
 6. Execute following commands
	+ pip install virtualenvwrapper-win
	+ mkvirtualenv autocompany
	+ workon autocompany
	+ pip install -r requirements.txt
	
7. Run the server using command,
	+ python manage.py runserver

8. Go to http://127.0.0.1:8000/  to view the app

9. Refer the site_overview.pdf for step by step instructions for site usability.
 	+ First Use "Register" link to register a user
 	+ Login to the account
	+ Go to products to see the overview of the products. Click on the Product name to view a full desciption of the products
	+ Add to cart and use the link "View Cart" to remove products or place an order
	+Placed orders and Listed products can be modified through the admin page
		- Go to http://127.0.0.1:8000/admin
		- Use the username "root" and password "1234" to acess the root user
	
	
	