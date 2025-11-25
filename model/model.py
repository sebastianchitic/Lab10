from database.dao import DAO
import networkx as nx

class Model:
    def __init__(self):
        self._nodes = None
        self._edges = None
        self.G = nx.Graph()

    def costruisci_grafo(self, threshold):
        """
        Costruisce il grafo (self.G) inserendo tutti gli Hub (i nodi) presenti e filtrando le Tratte con
        guadagno medio per spedizione >= threshold (euro)
        """
        self.G.clear()

        all_hubs = DAO.hub()
        for hub in all_hubs:
            self.G.add_node(hub.id, object=hub)

        all_connessioni = DAO.get_all_connessioni()

        for conn in all_connessioni:
            peso = conn['peso']

            if peso >= threshold:
                self.G.add_edge(conn['id1'], conn['id2'], weight=peso)



    def get_num_edges(self):
        """
        Restituisce il numero di Tratte (edges) del grafo
        :return: numero di edges del grafo
        """
        return self.G.number_of_edges()

    def get_num_nodes(self):
        """
        Restituisce il numero di Hub (nodi) del grafo
        :return: numero di nodi del grafo
        """
        return self.G.number_of_nodes()

    def get_all_edges(self):
        """
        Restituisce tutte le Tratte (gli edges) con i corrispondenti pesi
        :return: gli edges del grafo con gli attributi (il weight)
        """
        return self.G.edges(data=True)



