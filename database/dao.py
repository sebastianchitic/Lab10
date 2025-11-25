from xml.sax.handler import feature_namespaces

from database.DB_connect import DBConnect
from model.hub import Hub
from model.spedizione import Spedizione
from model.compagnia import Compagnia


class DAO:
    """
    Implementare tutte le funzioni necessarie a interrogare il database.
    """
    @staticmethod
    def compagnia():
        cnx = DBConnect.get_connection()
        result = []
        if cnx is None:
            print("errore di connessione")
            return None

        cursor = cnx.cursor(dictionary=True)
        query = """SELECT * FROM compagnia"""
        try:
            cursor.execute(query)
            for row in cursor:
                compagnia = Compagnia(
                    id = row["id"],
                    codice = row["codice"],
                    nome = row["nome"]
                )
                result.append(compagnia)
        except Exception as e:
            print("errore durante la query di compagnia")
            result = None
        finally:
            cursor.close()
            cnx.close()
        return result

    @staticmethod
    def hub():
        cnx = DBConnect.get_connection()
        result = []
        if cnx is None:
            print("errore di connessione")
            return None
        cursor = cnx.cursor(dictionary=True)
        query = """SELECT * FROM hub"""
        try:
            cursor.execute(query)
            for row in cursor:
                hub = Hub(
                    id = row["id"],
                    codice = row["codice"],
                    nome = row["nome"],
                    citta = row["citta"],
                    stato = row["stato"],
                    latitudine = row["latitudine"],
                    longitudine = row["longitudine"]
                )
                result.append(hub)
        except Exception as e:
            print("errore durante la query di hub")
            result = None
        finally:
            cursor.close()
            cnx.close()
        return result

    @staticmethod
    def spedizione():
        cnx = DBConnect.get_connection()
        result = []
        if cnx is None:
            print("errore di connessione")
            return None
        cursor = cnx.cursor(dictionary=True)
        query = """SELECT * FROM spedizione"""
        try:
            cursor.execute(query)
            for row in cursor:
                spedizione = Spedizione(
                    id = row["id"],
                    id_compagnia = row["id_compagnia"],
                    numero_tracking= row["numero_tracking"],
                    id_hub_origine=row["id_hub_origine"],
                    id_hub_destinazione=row["id_hub_destinazione"],
                    data_ritiro_programmata=row["data_ritiro_programmata"],
                    distanza = row["distanza"],
                    data_consegna = row["data_consegna"],
                    valore_merce=row["valore_merce"]
                )
                result.append(spedizione)
        except Exception as e:
            print("errore durante la query di spedizione")
            result = None
        finally:
            cursor.close()
            cnx.close()
        return result

    @staticmethod
    def get_all_connessioni():
        cnx = DBConnect.get_connection()
        result = []
        if cnx is None:
            print("errore di connessioni")
        cursor = cnx.cursor(dictionary=True)

        query = """SELECT
                    LEAST(id_hub_origine, id_hub_destinazione) as id1,
                    GREATEST(id_hub_origine, id_hub_destinazione) as id2,
                    AVG(valore_merce) as peso
                FROM spedizione
                GROUP BY id1, id2
                """
        try:
            cursor.execute(query)
            for row in cursor:
                result.append(row)
        except Exception as e:
            print("errore durante la query")
            result = None
        finally:
            cursor.close()
            cnx.close()
        return result





