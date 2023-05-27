from bson import ObjectId
from flask import Blueprint, request, jsonify
from datetime import datetime
from server_auth import auth
from utils import app_strings

## Created a new blueprint object in order to kept the implementation seperately.
noteOperations = Blueprint(app_strings.noteOperationsBlueprintName, __name__)

# METHOD: GET
# PURPOSE: Fetch all notes from server.
@noteOperations.route(app_strings.fetchAllNotesAppRoutePath, methods=[app_strings.restApiMethodGET])
def fetchAllNotes():
    database = auth.Auth.db_for_application()
    notes = database.NoteApplicationCollection.find({})
    serialized_notes = []
    for note in notes:
        note[app_strings.serverResponseFieldID] = str(note[app_strings.serverResponseFieldID])
        serialized_notes.append(note)
    return jsonify(serialized_notes)

# METHOD: POST
# PURPOSE: Create a new note and store it on server.
@noteOperations.route(app_strings.createNoteAppRoutePath, methods=[app_strings.restApiMethodPOST])
def createNote():
    database = auth.Auth.db_for_application()
    database.NoteApplicationCollection.insert_one(
        {
            app_strings.serverResponseFieldTitle:request.json[app_strings.serverResponseFieldTitle],
            app_strings.serverResponseFieldDetails:request.json[app_strings.serverResponseFieldDetails],
            app_strings.serverResponseFieldCreatedAt:datetime.now(),
            app_strings.serverResponseFieldLastUpdatedAt:datetime.now()
        }
    )
    return jsonify(message=app_strings.responseMessageCreatedNote)

# METHOD: PUT
# PURPOSE: Update a note as per the user's changes.
@noteOperations.route(app_strings.updateNoteAppRoutePath, methods=[app_strings.restApiMethodPUT])
def updateNote(note_id):
    data = request.get_json()
    data[app_strings.serverResponseFieldCreatedAt] = datetime.strptime(data[app_strings.serverResponseFieldCreatedAt], app_strings.date_format)
    data[app_strings.serverResponseFieldLastUpdatedAt] = datetime.now()
    database = auth.Auth.db_for_application()
    database.NoteApplicationCollection.replace_one({app_strings.serverResponseFieldID: ObjectId(note_id)}, data)
    return jsonify({app_strings.responseMessage: app_strings.responseMessageUpdateNote})

# METHOD: DELETE
# PURPOSE: Delete particular note from the server
@noteOperations.route(app_strings.deleteNoteAppRoutePath, methods=[app_strings.restApiMethodDELETE])
def deleteNote(note_id):
    database = auth.Auth.db_for_application()
    database.NoteApplicationCollection.delete_one({app_strings.serverResponseFieldID: ObjectId(note_id)})
    return jsonify({app_strings.responseMessage: app_strings.responseMessageDeleteNote})