import sqlite3


class TrackRepository:

    def __init__(self, table_name):
        self.table_name = table_name
        self.database_path = f"{self.table_name}.db"
        self.create_table()

    def create_table(self):
        with sqlite3.connect(self.database_path) as connection:
            cursor = connection.cursor()

            cursor.execute(
                f"""
                CREATE TABLE IF NOT EXISTS {self.table_name}
                (
                    id TEXT PRIMARY KEY,
                    audio TEXT
                )
                """
            )

            connection.commit()

    def clear_all_tracks(self):
        with sqlite3.connect(self.database_path) as connection:
            cursor = connection.cursor()

            cursor.execute(
                f"DELETE FROM {self.table_name}"
            )

            connection.commit()

    def insert_track(self, track_json):

        with sqlite3.connect(self.database_path) as connection:
            cursor = connection.cursor()

            cursor.execute(
                f"INSERT INTO {self.table_name} (id, audio) VALUES (?, ?)",
                (track_json["id"], track_json["audio"])
            )

            connection.commit()

            return cursor.rowcount

    def update_track(self, track_json):

        with sqlite3.connect(self.database_path) as connection:
            cursor = connection.cursor()

            cursor.execute(
                f"UPDATE {self.table_name} SET audio=? WHERE id=?",
                (track_json["audio"], track_json["id"])
            )

            connection.commit()

            return cursor.rowcount

    def get_track(self, track_id):

        with sqlite3.connect(self.database_path) as connection:
            cursor = connection.cursor()

            cursor.execute(
                f"SELECT id, audio FROM {self.table_name} WHERE id=?",
                (track_id,)
            )

            row = cursor.fetchone()

            if row:
                return {
                    "id": row[0],
                    "audio": row[1]
                }

            return None

    def delete_track(self, track_id):

        with sqlite3.connect(self.database_path) as connection:
            cursor = connection.cursor()

            cursor.execute(
                f"DELETE FROM {self.table_name} WHERE id=?",
                (track_id,)
            )

            connection.commit()

            return cursor.rowcount > 0

    def list_tracks(self):

        with sqlite3.connect(self.database_path) as connection:
            cursor = connection.cursor()

            cursor.execute(
                f"SELECT id FROM {self.table_name}"
            )

            return [row[0] for row in cursor.fetchall()]
