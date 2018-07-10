import sublime, sublime_plugin, math

class PromptBreakLinesCommand(sublime_plugin.WindowCommand):

    def run(self):
        self.window.show_input_panel("Break every X lines:", "", self.on_done, None, None)

    def on_done(self, text):
        try:
            break_gap = int(text)
            if self.window.active_view():
                self.window.active_view().run_command("break_lines", {"break_gap": break_gap} )
        except ValueError:
            pass

class BreakLinesCommand(sublime_plugin.TextCommand):

    def run(self, edit, break_gap):
        try:
            break_gap = int(break_gap)
            selections = [region for region in self.view.sel() if not region.empty()]

            if selections:
                # Break non-empty selections
                # Reverse the list or adding breaks will shift later lines
                [self.break_lines(edit, region, break_gap) for region in reversed(selections)]

            else:
                # If all selections were empty, break whole file
                all = sublime.Region(0, self.view.size())
                self.break_lines(edit, all, break_gap)
        except ValueError:
            pass


    def break_lines(self, edit, region, break_gap):
        first_line = self.view.rowcol(region.begin())[0]
        last_line = self.view.rowcol(region.end())[0]

        # Find how many breaks we can make, times it by the break gap, add to the start of our region
        last_changed_line = (math.floor((last_line - first_line) / break_gap) * break_gap) + first_line

        # Start with the last break, and go until we've finished with our region
        while (last_changed_line > first_line):
            self.view.insert(edit, self.view.text_point(last_changed_line, 0), '\n')
            last_changed_line -= break_gap