from tkinter import *
from tkinter import ttk
from tkinter.font import Font

from Vistas.Util_tk import Util


class MCListDemo(ttk.Frame):
    # class variable to track direction of column
    # header sort
    SortDir = True  # descending

    def __init__(self, master, tipo = '', isapp=True, name='mclistdemo',):
        ttk.Frame.__init__(self, name=name, master = master)
        self.grid(row=18, sticky=N)
        self.isapp = isapp
        self.items= {}
        self.tipo= tipo
        self._create_widgets()

    def _create_widgets(self):
        if self.isapp:
            'meeh'

        self._create_demo_panel()

    def _create_demo_panel(self):
        demoPanel = Frame(self)
        demoPanel.pack(side=TOP, fill=BOTH, expand=False)

        self._create_treeview(demoPanel)
        self._load_data()

    def _create_treeview(self, parent):
        f = ttk.Frame(parent)
        f.pack(side=TOP, fill=BOTH, expand=False)

        # create the tree and scrollbars
        self.dataCols = Util.get_titulo(self.tipo)
        self.tree = ttk.Treeview(columns=self.dataCols, show='headings')


        ysb = ttk.Scrollbar(orient=VERTICAL, command=self.tree.yview)
        xsb = ttk.Scrollbar(orient=HORIZONTAL, command=self.tree.xview)
        self.tree['yscroll'] = ysb.set
        self.tree['xscroll'] = xsb.set

        # add tree and scrollbars to frame
        self.tree.grid(in_=f, row=0, column=0, sticky=NSEW)
        ysb.grid(in_=f, row=0, column=1, sticky=NS)
        xsb.grid(in_=f, row=1, column=0, sticky=EW)

        # set frame resize priorities
        f.rowconfigure(0, weight=1)
        f.columnconfigure(0, weight=1)


    def _load_data(self):
        lista = Util.get_lista(self.tipo)

        if lista != None:

            # configure column headings
            for c in self.dataCols:
                self.tree.heading(c, text=c.title(),
                                  command=lambda c=c: self._column_sort(c,
                                                                        MCListDemo.SortDir))
                self.tree.column(c, width=Font().measure(c.title()))

            # add data to the tree
            for item in lista:
                self.tree.insert('', 'end', values=item)

            '''
            # and adjust column widths if necessary
            for idx, val in enumerate(item):
                iwidth = Font().measure(val)
                if self.tree.column(self.dataCols[idx], 'width') < iwidth:
                            self.tree.column(self.dataCols[idx], width=iwidth)
            '''


    def _column_sort(self, col, descending=False):

        # grab values to sort as a list of tuples (column value, column id)
        # e.g. [('Argentina', 'I001'), ('Australia', 'I002'), ('Brazil', 'I003')]
        data = [(self.tree.set(child, col), child) for child in
                self.tree.get_children('')]

        # reorder data
        # tkinter looks after moving other items in
        # the same row
        data.sort(reverse=descending)
        for indx, item in enumerate(data):
            self.tree.move(item[1], '', indx)  # item[1] = item Identifier

        # reverse sort direction for next sort operation
        MCListDemo.SortDir = not descending


    def cargar_item(self, item):
        for i, var in enumerate(item):
            id = self.tree.insert('', 'end', value=item[i])
            self.items[id] = item

    def eliminar_fila(self, fila):
        self.tree.delete(fila)

    def selecion_item(self):
        #return the data of  the first column
        selected_item = self.tree.item(self.tree.selection())['values'][0]
        return selected_item

    def get_item_raw(self):
        fila = self.tree.selection()[0]  # get fila
        return fila

    def comprobar_item(self):
        return self.tree.get_children()




if __name__ == '__main__':
    MCListDemo().mainloop()