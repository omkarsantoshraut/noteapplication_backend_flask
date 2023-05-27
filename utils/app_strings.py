Alpha_Main_Database = 'NoteApplicationDB'

## database link
database_connection_link = 'mongodb+srv://%s:%s@cluster0.oosdwho.mongodb.net/?retryWrites=true&w=majority'

database_connection_fail = 'Fail to connect to database/server.'

#### CRUD operations
noteOperationsBlueprintName = 'noteOperations'


#### ROUTES
fetchAllNotesAppRoutePath = '/notes'
createNoteAppRoutePath = '/createNote'
updateNoteAppRoutePath = '/updateNote/<note_id>'
deleteNoteAppRoutePath = '/deleteNote/<note_id>'

#### RESPONSE MESSAGES
responseMessage = 'message'
responseMessageCreatedNote = 'Note created successfully.'
responseMessageUpdateNote = 'Note updated successfully'
responseMessageDeleteNote = 'Note deleted successfully'

#### REST API METHODS
restApiMethodGET = 'GET'
restApiMethodPOST = 'POST'
restApiMethodPUT = 'PUT'
restApiMethodDELETE = 'DELETE'

#### SERVER RESPONSE FIELDS
date_format = '%a, %d %b %Y %H:%M:%S %Z'
serverResponseFieldID = '_id'
serverResponseFieldTitle = 'title'
serverResponseFieldDetails = 'details'
serverResponseFieldCreatedAt = 'createdAt'
serverResponseFieldLastUpdatedAt = 'lastUpdatedAt'