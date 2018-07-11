import sublime, sublime_plugin, math

class PromptBreakLinesCommand(sublime_plugin.TextCommand):

    def run(self, edit):
        self.view.window().show_input_panel("Break every X lines:", "", self.on_done, None, None)

    def on_done(self, text):
        try:
            break_gap = int(text)
            self.view.run_command("break_lines", {"break_gap": break_gap} )
        except ValueError:
            pass

class BreakLinesCommand(sublime_plugin.TextCommand):

    def run(self, edit, break_gap):
        selections = [region for region in self.view.sel() if not region.empty()]

        if selections:
            # Break non-empty selections
            # Reverse the list or adding breaks will shift later lines
            [self.break_lines(edit, region, break_gap) for region in reversed(selections)]

        else:
            # If all selections were empty, break whole file
            all = sublime.Region(0, self.view.size())
            self.break_lines(edit, all, break_gap)


    def break_lines(self, edit, region, break_gap):
        first_line = self.view.rowcol(region.begin())[0]
        last_line = self.view.rowcol(region.end())[0]

        # Every break_gap steps after the first line up to and including the last line, add a newline
        # Reverse the list or adding breaks will shift later lines
        for line_to_change in reversed(range(first_line + break_gap, last_line + 1, break_gap)):
            self.view.insert(edit, self.view.text_point(line_to_change, 0), '\n')