from database_manager import DatabaseManager


INSERT_STATE_TEMPLATE = "INSERT INTO state (state_name) VALUES (\"{0}\");"
DELETE_STATES_TEMPLATE = "DELETE FROM state;"
SELECT_STATES_TEMPLATE = "SELECT id, state_name FROM state;"


class State:
    def __init__(self, state_id, state_name):
        self.state_id = state_id
        self.state_name = state_name


class StateDAO:
    @staticmethod
    def delete_data():
        # get connection to database
        db_conn = DatabaseManager.get_connection()
        cursor = db_conn.cursor()

        # delete state records
        cursor.execute(DELETE_STATES_TEMPLATE)

        # commit transaction
        db_conn.commit()

        # close cursor and connection
        cursor.close()
        db_conn.close()

    def __init__(self):
        self.state_data = {}

        self.update()

    def get_state_by_name(self, state_name):
        for state in self.state_data.values():
            if state_name == state.state_name:
                return state

        return None

    def insert_data(self, state_name):
        # check to see if state already exists
        state = self.get_state_by_name(state_name)
        if state is not None:
            return state

        # insert new state data
        db_conn = DatabaseManager.get_connection()
        cursor = db_conn.cursor()
        cursor.execute(INSERT_STATE_TEMPLATE.format(state_name))
        state_id = cursor.lastrowid

        # create State object
        state = State(state_id, state_name)

        # update state_data dictionary; there should only be one record
        # created per state
        self.state_data[state_id] = state

        # commit changes
        db_conn.commit()

        # close cursor and connection
        cursor.close()
        db_conn.close()

        # return new state
        return state

    def update(self):
        # clear state dictionary
        self.state_data.clear()

        # retrieve state records from database
        db_conn = DatabaseManager.get_connection()
        cursor = db_conn.cursor()
        cursor.execute(SELECT_STATES_TEMPLATE)

        # create State objects from records
        for (id, state_name) in cursor:
            self.state_data[int(id)] = State(int(id), state_name)

        # close connection and cursor
        cursor.close()
        db_conn.close()
