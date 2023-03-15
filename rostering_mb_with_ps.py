# diagram.py
from diagrams import Diagram, Cluster, Edge
from diagrams.custom import Custom
from diagrams.aws.compute import EC2
from diagrams.aws.database import RDS
from diagrams.aws.network import ELB
from diagrams.gcp.api import Endpoints

main_edge = lambda label=None: Edge(color='purple', label=label)
internal_edge = lambda: Edge(color='darkgreen', label='internal')
http_edge = lambda: Edge(color='darkgrey')

with Diagram("System Diagram: PS > MB", show=True, direction="LR"):
    with Cluster('mbpy'):
        mbpy = Custom("api interface", 'logos/code.png')
        algorithm = Custom('algorithm', 'logos/code.png')
        mbpy2 = Custom("api interface", 'logos/code.png')

    with Cluster("PowerSchool"):
        ps_plugin = Custom('PS plugin', 'logos/code.png')
        ps_app = Custom("PS app", 'logos/ps.png')
        ps_plugin >> internal_edge() << ps_app
        mbpy >> http_edge() << ps_plugin

    with Cluster('ManageBac (read)'):
        mb_api = Endpoints('Public REST API')
        mb_app = Custom("MB app", 'logos/mb.png')
        mb_api >> internal_edge() << mb_app
        mbpy >> http_edge() << mb_api

    with Cluster('Managebac (write)'):
        mb_api2 = Endpoints('Public REST API')
        mb_app2 = Custom("MB app", 'logos/mb.png')

        mbpy >> main_edge() >> algorithm >> main_edge(label="Update this only") >> mbpy2 >> main_edge() >> mb_api2
        mb_api2 >> internal_edge() << mb_app2


