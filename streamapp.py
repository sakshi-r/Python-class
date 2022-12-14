from git import Commit
import streamlit as st
from sqlalchemy.orm import sessionmaker
from sqlalchemy import create_engine
form database import Author

def opendb():
    engine= create_engine('sqlite:///mydb.sqlite')
    session= sessionmaker(bind=engine)
    return session()

def add_author(name):
    db= opendb()
    a= Author(name=name)
    db.add(a)
    db.commit()
    db.close()

def show_authors():
    db= opendb()
    authors= db.query(Author).all()
    db.close()
    return authors

def delete_author(name):
    try:
        db= opendb()
        a= db.query(Author).filter_by(name=name).first()
        db.delete(a)
        db.commit()
        db.close()
        print('Author deleted')
    except:
        print('author not found')
st.title("Books App")
st.subheader("will use database to load and save data")
choices= ['List authors', 'Add author', 'Delete author']
choice= st.sidebar.selectbox('Select an option', choices)

if choice== choices[0]:
    for author in show_authors():
        st.subheader(f"{author.id}. {author.name}")
elif choice== choices[1]:
    name= st.text_input('Enter author name:')
elif choice== choices[2]:
    name= st.text_input('Enter author name:')
    if name:
        if delete_author(name):
            st.success('Author deleted')
        else:
            st.error('Author not found')
    else:
        st.warning('Please enter the author name')
