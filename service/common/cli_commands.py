"""
Flask CLI Command Extensions
"""
from service import app
from service.models import db


######################################################################
# Command to force tables to be rebuilt
# Usage:
#   flask db-create
######################################################################
@app.cli.command("db-create")
def db_create():
    """
    Recreates a local database. You probably should not use this on
    production. ;-)
    """
    print("Running drop_all")
    db.drop_all()
    
    print("Running create_all")
    db.create_all()

    print("Running session.commit")
    db.session.commit()
