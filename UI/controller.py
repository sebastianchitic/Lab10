import flet as ft
from UI.view import View
from model.model import Model


class Controller:
    def __init__(self, view: View, model: Model):
        self._view = view
        self._model = model

    def mostra_tratte(self, e):
        """
        Funzione che controlla prima se il valore del costo inserito sia valido (es. non deve essere una stringa) e poi
        popola "self._view.lista_visualizzazione" con le seguenti info
        * Numero di Hub presenti
        * Numero di Tratte
        * Lista di Tratte che superano il costo indicato come soglia
        """
        try:
            soglia = float(self._view.guadagno_medio_minimo.value)
        except ValueError:
            return

        self._model.costruisci_grafo(soglia)

        n_nodi = self._model.get_num_nodes()
        n_archi = self._model.get_num_edges()
        archi_con_pesi = self._model.get_all_edges()

        self._view.lista_visualizzazione.clean()

        self._view.lista_visualizzazione.controls.append(ft.Text(f"Numero di nodi: {n_nodi}"))
        self._view.lista_visualizzazione.controls.append(ft.Text(f"Numero di archi: {n_archi}"))

        for u,v,data in archi_con_pesi:
            peso = data['weight']

            nodo_u = self._model.G.nodes[u]['object']
            nodo_v = self._model.G.nodes[v]['object']

            riga = ft.Text(f"{nodo_u} - {nodo_v} | Guadagno medio: {peso:.2f}$")
            self._view.lista_visualizzazione.controls.append(riga)

        self._view.update()



