import sqlite3
import os
import xml.etree.ElementTree as ET


# # Email count per Organization
# conn = sqlite3.connect('org_count.sqlite')
# cur = conn.cursor()
#
# cur.execute('DROP TABLE IF EXISTS Counts')
# cur.execute('CREATE TABLE Counts (org TEXT, count INTEGER)')
#
# file_name = input('Enter file name: ')
# if len(file_name) < 1:
#     file_name = 'mbox.txt'
# file_hand = open(f'C:\\Users\\Deadp\\Desktop\\freeCodeCamp\\Scientific_Computing_Python\\Exercises\\text_files\\{file_name}')
#
# for i, lines in enumerate(file_hand.readlines()):
#     if lines.startswith("From:"):
#         org = lines.split()[1].split('@')[1]
#         cur.execute('SELECT count FROM Counts WHERE org = ?', (org,))
#         row = cur.fetchone()
#         if row is None:
#             cur.execute('INSERT INTO Counts (org, count) VALUES (?, 1)', (org,))
#         else:
#             cur.execute('UPDATE Counts SET count = count + 1 WHERE org = ?', (org,))
#     # commit every 5000 lines/inserts
#     # if i % 5000 == 0:
# conn.commit()
# cur.close()

# # Musical Track Database
# conn = sqlite3.connect('music_track.sqlite')
# cur = conn.cursor()
#
# cur.executescript('''
# DROP TABLE IF EXISTS Artist;
# DROP TABLE IF EXISTS Genre;
# DROP TABLE IF EXISTS Track;
# DROP TABLE IF EXISTS Album;
#
# CREATE TABLE Artist (
#     id  INTEGER NOT NULL PRIMARY KEY AUTOINCREMENT UNIQUE,
#     name    TEXT UNIQUE
# );
#
# CREATE TABLE Genre (
#     id  INTEGER NOT NULL PRIMARY KEY AUTOINCREMENT UNIQUE,
#     name    TEXT UNIQUE
# );
#
# CREATE TABLE Album (
#     id  INTEGER NOT NULL PRIMARY KEY AUTOINCREMENT UNIQUE,
#     artist_id  INTEGER,
#     title   TEXT UNIQUE
# );
#
# CREATE TABLE Track (
#     id  INTEGER NOT NULL PRIMARY KEY
#         AUTOINCREMENT UNIQUE,
#     title TEXT  UNIQUE,
#     album_id  INTEGER,
#     genre_id  INTEGER,
#     len_secs INTEGER, rating INTEGER, count INTEGER
# );
# ''')
#
# file_name = input('Enter file name: ')
# if len(file_name) < 1:
#     file_name = 'Library.xml'
# tree = ET.parse(file_name)
# root = tree.findall('dict/dict/dict')
#
#
# # Func for parsing through tags in XML
# def lookup(parent, _key, found=False):
#     for child in parent:
#         if found: return child.text
#         if child.tag == 'key' and child.text == _key: found = True
#     return None
#
#
# for i, keys in enumerate(root):
#     if lookup(keys, 'Track ID') is None: continue
#     # Variables for database after parsing XML
#     artist = lookup(keys, 'Artist')
#     genre = lookup(keys, 'Genre')
#     album = lookup(keys, 'Album')
#     track = lookup(keys, 'Name')
#     length = lookup(keys, 'Total Time')
#     rating = lookup(keys, 'Rating')
#     count = lookup(keys, 'Play Count')
#
#     if track is None or artist is None or album is None or genre is None or length is None: continue
#     length = ':'.join(f'{int(length)/1000:.2f}'.split('.'))
#
#     cur.execute('INSERT OR IGNORE INTO Artist (name) VALUES (?)', (artist,))
#     cur.execute('SELECT id FROM Artist WHERE name = ? ', (artist,))
#     artist_id = cur.fetchone()[0]
#
#     cur.execute('INSERT OR IGNORE INTO Genre (name) VALUES (?)', (genre,))
#     cur.execute('SELECT id FROM Genre WHERE name = ?', (genre,))
#     genre_id = cur.fetchone()[0]
#
#     cur.execute('INSERT OR IGNORE INTO Album (artist_id, title) VALUES (?,?)', (artist_id, album))
#     cur.execute('SELECT id FROM Album WHERE title = ?', (album,))
#     album_id = cur.fetchone()[0]
#
#     cur.execute('INSERT OR IGNORE INTO Track (title, album_id, genre_id, len_secs, rating, count) VALUES (?,?,?,?,?,?)', (track, album_id, genre_id, length, rating, count))
# conn.commit()
# conn.close()
# cur.close()

# Many Students in many places

# import json
# import sqlite3
#
# conn = sqlite3.connect('Many_students.sqlite')
# cur = conn.cursor()
#
# cur.executescript('''
# DROP TABLE IF EXISTS User;
# DROP TABLE IF EXISTS Member;
# DROP TABLE IF EXISTS Course;
#
# CREATE TABLE User (
#     id      INTEGER NOT NULL PRIMARY KEY AUTOINCREMENT UNIQUE,
#     name    TEXT UNIQUE
# );
#
# CREATE TABLE Course (
#     id      INTEGER NOT NULL PRIMARY KEY AUTOINCREMENT UNIQUE,
#     title   TEXT UNIQUE
# );
#
# CREATE TABLE Member (
#     user_id     INTEGER,
#     course_id   INTEGER,
#     role        INTEGER,
#     PRIMARY KEY (user_id, course_id)
# )
# ''')
#
# file_name = input('Enter file name: ')
# if len(file_name) < 1:
#     file_name = 'roster_data.json'
#
# file_data = open(file_name).read()
# json_data = json.loads(file_data)
#
# for index, user, course, role in enumerate(json_data):
#     cur.execute('INSERT OR IGNORE INTO User (name) VALUES (?)', (user,))
#     cur.execute('SELECT id FROM User WHERE name = ?', (user,))
#     user_id = cur.fetchone()[0]
#
#     cur.execute('INSERT OR IGNORE INTO Course (title) VALUES (?)', (course,))
#     cur.execute('SELECT id FROM Course WHERE title = ?', (course,))
#     course_id = cur.fetchone()[0]
#
#     cur.execute('INSERT OR REPLACE INTO Member (user_id, course_id, role) VALUES (?, ?, ?)', (user_id, course_id, role))
#     if index % 25 == 0:
#         conn.commit()
#
# cur.close()
# conn.close()

