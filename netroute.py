#!/usr/bin/env python
# coding:utf-8

"""
netroute.py
"""


import re
import subprocess as sp
import socket
import folium
import geoip2.database
from graphviz import Digraph


class NetRoute(object):
    """
    NetRoute

    Note
    ----------
    a

    Args
    ----------
    target : str
        target ip address or hostname
    __ip_list : dict{int : list[str(ip)]}
        ip address list, key -> hop
    __address_list : dict{str(ip) : list[float, float]}
    Attributes
    ----------
    run : none
        run exec cmd, and plot network graph
    """

    def __init__(self, target):
        self.target = target
        self.__ip_list = dict()
        self.__address_list = dict()

    def run(self):
        """
        run

        Parameters
        ----------
        none
        Returns
        -------
        none
        """

        # traceroute
        res = self.__exec_cmd("traceroute " + self.target).split("\n")
        self.__ip_list = {0: [socket.gethostbyname(socket.gethostname())]}
        index = 0
        for s in res[:-1]:
            # s の先頭2文字が空白以外(数字)か確認．
            if s[:2] != "  ":
                index += 1
                self.__ip_list[index] = [self.__extraction_ip(s)]
            else:
                self.__ip_list[index].append(self.__extraction_ip(s))

        for node in self.__ip_list:
            self.__ip_list[node] = list(set(self.__ip_list[node]))
            for ip in self.__ip_list[node]:
                self.__address_list[ip] = self.__ip_to_coordinate(ip)
            print(str(node) + " : " + str(self.__ip_list[node]))
        self.__generate_graph()
        self.__generate_map()

    def __extraction_ip(self, text):
        """
        __extraction_ip

        Parameters
        ----------
        none
        Returns
        -------
        none
        """

        ip = re.search("[(][0-9]+.[0-9]+.[0-9]+.[0-9]+[)]", text).group(0)
        return ip.replace("(", "").replace(")", "")

    def __exec_cmd(self, cmd):
        """
        __exec_cmd
        private method
        Exec Shell Command

        Parameters
        ----------
        cmd : str
            shell command
        Returns
        -------
        stdout/stderr : str
            shell command output
        """

        print(cmd + "\n")
        res = sp.Popen(cmd, shell=True, stdout=sp.PIPE)
        stdout, strerr = res.communicate()
        if strerr is None:
            return stdout.decode("UTF-8")
        else:
            return strerr.decode("UTF-8")

    def __generate_graph(self):
        """
        generate_graph
        generate graph from self.__ip_list
        graph -> .png

        Parameters
        ----------
        none
        Returns
        -------
        none
        """

        G = Digraph(format="png")
        G.attr("node", shape="box", width="1", color="black")
        for node in self.__ip_list:
            if node != 0 and node != len(self.__ip_list)-1:
                for ip in self.__ip_list[node]:
                    G.node(ip)
            else:
                G.node(self.__ip_list[node][0], shape="oval", color="blue")
        for node in self.__ip_list:
            if node != len(self.__ip_list)-1:
                for start_ip in self.__ip_list[node]:
                    for dist_ip in self.__ip_list[node + 1]:
                        G.edge(start_ip, dist_ip)
        G.render("traceroute_fig_" + self.target)

    def __generate_map(self):
        """
        generate_map

        Parameters
        ----------
        none
        Returns
        -------
        none
        """

        map_net = folium.Map(location=[35, 139], zoom_start=1)
        for node in self.__ip_list:
            if node == 0:
                pass
            else:
                for ip in self.__ip_list[node]:
                    name = str(node) + " : " + ip
                    pos = self.__address_list[ip]
                    if pos is not None:
                        folium.Marker(location=pos, popup=name).add_to(map_net)

        map_net.save("traceroute_map_" + self.target + ".html")

    def __ip_to_coordinate(self, ip_address):
        """
        ip_to_coordinate

        Parameters
        ----------
        ip_address : str
            ip address
        Returns
        -------
        lat : float
            latitude
        lng : float
            longitude
        """

        try:
            reader = geoip2.database.Reader("GeoLite2-City.mmdb")
            record = reader.city(ip_address)
        except FileNotFoundError:
            print("File Not Found")
        except geoip2.errors.AddressNotFoundError:
            print(ip_address + " is not in the database")
        else:
            lat = record.location.latitude
            lng = record.location.longitude
            return [lat, lng]


if __name__ == "__main__":
    import sys
    args = sys.argv
    assert len(args) == 2, "USAGE : python netroute.py target(IP/HOST)"
    nr = NetRoute(args[1])
    nr.run()
