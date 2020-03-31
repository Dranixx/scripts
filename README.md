# Scripts
All scripts that I use.

## How to use
For Python script:  
Create a venv
> virtualenv venv  
> source venv/bin/activate

Install requirements needed from each folders
> pip install -r folder/requirements.txt

## Details

- notion-clear-trash:  
  * Go to notion.so
  * Open developer tools (hit F12)
  * Navigate to the Application tab (may be hidden if the developer         windowissmall)
  * Expand Cookies under the Storage section on the sidebar
  * Click on 'https://www.notion.so' to view all the cookies
  * Copy the value for the key 'token_v2'
- img-date-reset:
  > date_reset.py [foler path]
