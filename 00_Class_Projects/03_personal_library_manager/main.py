import streamlit as st
import sqlite3

def create_db():
    conn = sqlite3.connect("books.db")
    cursor = conn.cursor()
    cursor.execute("""
        CREATE TABLE IF NOT EXISTS books (
            id INTEGER PRIMARY KEY AUTOINCREMENT,
            title TEXT,
            author TEXT,
            year TEXT,
            genre TEXT,
            read INTEGER
        )
    """)
    conn.commit()
    conn.close()

def add_book(title, author, year, genre, read):
    conn = sqlite3.connect("books.db")
    cursor = conn.cursor()
    cursor.execute("INSERT INTO books (title, author, year, genre, read) VALUES (?, ?, ?, ?, ?)", (title, author, year, genre, read))
    conn.commit()
    conn.close()

def get_books():
    conn = sqlite3.connect("books.db")
    cursor = conn.cursor()
    cursor.execute("SELECT * FROM books")
    books = cursor.fetchall()
    conn.close()
    return books

def delete_book(book_id):
    conn = sqlite3.connect("books.db")
    cursor = conn.cursor()
    cursor.execute("DELETE FROM books WHERE id=?", (book_id,))
    conn.commit()
    conn.close()

def update_book(book_id, title, author, year, genre, read):
    conn = sqlite3.connect("books.db")
    cursor = conn.cursor()
    cursor.execute("UPDATE books SET title=?, author=?, year=?, genre=?, read=? WHERE id=?", (title, author, year, genre, read, book_id))
    conn.commit()
    conn.close()

def main():
    st.set_page_config(page_title="Personal Library", page_icon="📚")
    st.title("📚 Book Collection Manager")
    create_db()
    
    menu = ["Add Book", "View Books", "Update Book", "Delete Book", "Reading Progress"]
    choice = st.sidebar.selectbox("Menu", menu)
    
    if choice == "Add Book":
        st.subheader("Add a New Book")
        title = st.text_input("Book Title")
        author = st.text_input("Author")
        year = st.text_input("Publication Year")
        genre = st.text_input("Genre")
        read = st.checkbox("Have you read this book?")
        if st.button("Add Book"):
            add_book(title, author, year, genre, int(read))
            st.success("Book added successfully!")
    
    elif choice == "View Books":
        st.subheader("Your Book Collection")
        books = get_books()
        if books:
            for book in books:
                st.write(f"**{book[1]}** by {book[2]} ({book[3]}) - {book[4]} - {'Read' if book[5] else 'Unread'}")
        else:
            st.write("No books in the collection.")
    
    elif choice == "Update Book":
        st.subheader("Update Book Details")
        books = get_books()
        book_dict = {book[1]: book for book in books}
        selected_book = st.selectbox("Select a book to update", list(book_dict.keys()))
        if selected_book:
            book = book_dict[selected_book]
            new_title = st.text_input("New Title", book[1])
            new_author = st.text_input("New Author", book[2])
            new_year = st.text_input("New Year", book[3])
            new_genre = st.text_input("New Genre", book[4])
            new_read = st.checkbox("Have you read this book?", bool(book[5]))
            if st.button("Update Book"):
                update_book(book[0], new_title, new_author, new_year, new_genre, int(new_read))
                st.success("Book updated successfully!")
    
    elif choice == "Delete Book":
        st.subheader("Delete a Book")
        books = get_books()
        book_dict = {book[1]: book for book in books}
        selected_book = st.selectbox("Select a book to delete", list(book_dict.keys()))
        if selected_book:
            book = book_dict[selected_book]
            if st.button("Delete Book"):
                delete_book(book[0])
                st.success("Book deleted successfully!")
    
    elif choice == "Reading Progress":
        st.subheader("Reading Progress")
        books = get_books()
        total_books = len(books)
        completed_books = sum(1 for book in books if book[5])
        completion_rate = (completed_books / total_books * 100) if total_books else 0
        st.write(f"Total books: {total_books}")
        st.write(f"Reading progress: {completion_rate:.2f}%")

    st.markdown("---")
    st.write("Build with ❤ by [Muhammad Kamran](https://github.com/KamranYT)")
if __name__ == "__main__":
    main()

