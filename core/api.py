class Api:
    """Api class for plugins

    Attributes:
        main_window (MainWindow): MainWindow object
    """

    def __init__(self, main_window):
        """Inits Api."""
        self.main_window = main_window

    def add_bookmark(self, bookmark, replace=False):
        """Adds a new bookmark to bookmark table

        Args:
            new_bookmark (Bookmark): A new bookmark
            replace (bool): Replace an existing bookmark if found on same row?
                Defaults to False.
        """
        self.main_window.trace_data.add_bookmark(bookmark, replace)

    def ask_user(self, title: str, question: str):
        """Shows a messagebox with yes/no question

        Args:
            title (str): MessageBox title
            question (str): MessageBox question label
        Returns:
            bool: True if user clicked yes, False otherwise
        """
        return self.main_window.ask_user(title, question)

    def get_bookmarks(self):
        """Returns all bookmarks

        Returns:
            list: List of Bookmark objects
        """
        return self.main_window.trace_data.get_bookmarks()

    def get_filtered_trace(self):
        """Returns filtered_trace"""
        return self.main_window.filtered_trace

    def get_full_trace(self):
        """Returns full trace from TraceData object"""
        return self.main_window.trace_data.trace

    def get_main_window(self):
        """Returns main_window object"""
        return self.main_window

    def get_string_from_user(self, title: str, label: str):
        """Get string from user.

        Args:
            title (str): Input dialog title
            label (str): Input dialog label
        Returns:
            string: String given by user
        """
        return self.main_window.get_string_from_user(title, label)

    def get_values_from_user(self, title: str, data: list, on_ok_clicked=None):
        """Get input from user. Data types: str, int, list, bool.

        Args:
            title (str): Input dialog title
            data (list): List of dicts describing labels and data
            on_ok_clicked (method): Callback function to e.g. check the input
        Returns:
            list: List of values, empty list if canceled
        """
        return self.main_window.get_values_from_user(title, data, on_ok_clicked)

    def get_selected_bookmarks(self):
        """Returns list of selected bookmarks"""
        return self.main_window.get_selected_bookmarks()

    def get_selected_trace(self):
        """Returns list of selected trace"""
        row_ids = self.get_selected_trace_row_ids()
        trace_data = self.get_trace_data()
        trace = trace_data.get_trace_rows(row_ids)
        return trace

    def get_selected_trace_row_ids(self):
        """Returns list of ids of selected rows"""
        return self.main_window.get_selected_row_ids(self.main_window.trace_table)

    def get_trace_data(self):
        """Returns TraceData object"""
        return self.main_window.trace_data

    def get_visible_trace(self):
        """Returns visible trace, either full or filtered trace"""
        return self.main_window.get_visible_trace()

    def get_regs(self):
        """Returns dictionary of registers and their indexes"""
        return self.main_window.trace_data.get_regs()

    def go_to_row_in_full_trace(self, row_id: int):
        """Goes to given row in full trace

        Args:
            row_id (int): Row id
        """
        self.main_window.go_to_row_in_full_trace(row_id)

    def go_to_row_in_current_trace(self, row_index: int):
        """Goes to given row index in currently visible trace (full or filtered)

        Args:
            row_index (int): Row index in trace
        """
        self.main_window.go_to_row_in_visible_trace(row_index)

    def print(self, text: str):
        """Prints text to log

        Args:
            text (str): Text to print in log
        """
        self.main_window.print(str(text))

    def set_comment(self, row: int, comment: str):
        """Sets a comment to trace

        Args:
            row (int): A row index in full trace
            comment (str): A comment text
        """
        try:
            self.main_window.trace_data.trace[row]["comment"] = str(comment)
        except IndexError:
            print(f"Error. Could not set comment to row {row}")

    def set_filtered_trace(self, trace):
        """Sets filtered_trace

        Args:
            trace (list): List of trace rows
        """
        self.main_window.filtered_trace = trace

    def show_filtered_trace(self):
        """Shows filtered trace on trace_table"""
        self.main_window.show_filtered_trace()

    def show_messagebox(self, title: str, msg: str):
        """Shows a messagebox

        Args:
            title (str): Title of messagebox
            msg (str): Message to show
        """
        self.main_window.show_messagebox(title, msg)

    def update_trace_table(self):
        """Updates trace_table"""
        self.main_window.trace_table.update()

    def update_bookmark_table(self):
        """Updates bookmark_table"""
        self.main_window.update_bookmark_table()
