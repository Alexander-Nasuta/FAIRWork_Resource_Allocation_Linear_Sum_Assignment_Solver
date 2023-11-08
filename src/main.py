from logger import log
import pprint
import random
import time
from ortools.graph.python import linear_sum_assignment

stevedore_suitability = {
    "100001": True,
    "100002": False,
    "100003": True,
    "100004": False,
    "100005": True,
    "100006": True,
    "100007": False,
    "100008": True,
    "100009": True,
    "100010": True,
    "100011": True,
    "100012": False,
    "100013": True,
    "100014": True,
    "100015": True,
    "100016": True,
    "100017": False,
    "100018": False,
    "100019": False,
    "100020": True,
    "100021": True,
    "100022": True,
    "100023": True,
    "100024": True,
    "100025": False,
    "100026": False,
    "100027": True,
    "100028": False,
    "100029": True,
    "100030": True,
    "100031": True,
    "100032": False,
    "100033": False,
    "100034": True,
    "100035": True,
    "100036": True,
    "100037": True,
    "100038": True,
    "100039": True,
    "100040": False,
    "100041": False,
    "100042": False,
    "100043": True,
    "100044": True,
    "100045": True,
    "100046": False,
    "100047": False,
    "100048": True,
    "100049": True,
    "100050": True,
    "100051": True,
    "100052": True,
    "100053": True,
    "100054": True,
    "100055": True,
    "100056": True,
    "100057": True,
    "100058": True,
    "100059": True,
    "100060": True,
    "100061": True,
    "100062": False,
    "100063": True,
    "100064": True,
    "100065": True,
    "100066": True,
    "100067": True,
    "100068": False,
    "100069": False,
    "100070": True,
    "100071": False,
    "100072": True,
    "100073": True,
    "100074": True,
    "100075": True,
    "100076": True,
    "100077": True,
    "100078": False,
    "100079": True,
    "100080": True,
    "100081": True,
    "100082": True,
    "100083": False,
    "100084": True,
    "100085": False,
    "100086": True,
    "100087": True,
    "100088": False,
    "100089": False,
    "100090": False,
    "100091": False,
    "100092": False,
    "100093": True,
    "100094": False,
    "100095": True,
    "100096": True,
    "100097": True,
    "100098": True,
    "100099": True,
    "100100": False,
    "100101": True,
    "100102": True,
    "100103": False,
    "100104": True,
    "100105": False,
    "100106": True,
    "100107": False,
    "100108": True,
    "100109": True,
    "100110": True,
    "100111": True,
    "100112": True,
    "100113": True,
    "100114": True,
    "100115": False,
    "100116": True,
    "100117": False,
    "100118": True,
    "100119": True,
    "100120": True,
    "100121": False,
    "100122": True,
    "100123": True,
    "100124": True,
    "100125": True,
    "100126": False,
    "100127": True,
    "100128": False,
    "100129": True,
    "100130": True,
    "100131": False,
    "100132": True,
    "100133": False,
    "100134": True,
    "100135": False,
    "100136": False,
    "100137": True,
    "100138": True,
    "100139": True,
    "100140": False,
    "100141": True,
    "100142": True,
    "100143": True,
    "100144": True,
    "100145": False,
    "100146": False,
    "100147": True,
    "100148": True,
    "100149": True,
    "100150": True,
    "100151": True,
    "100152": True,
    "100153": False,
    "100154": True,
    "100155": False,
    "100156": True,
    "100157": False,
    "100158": True,
    "100159": True,
}

UTE_4_experience = {
    "100001": False,
    "100002": False,
    "100003": True,
    "100004": True,
    "100005": True,
    "100006": True,
    "100007": True,
    "100008": True,
    "100009": True,
    "100010": True,
    "100011": True,
    "100012": True,
    "100013": True,
    "100014": True,
    "100015": True,
    "100016": False,
    "100017": False,
    "100018": False,
    "100019": False,
    "100020": False,
    "100021": False,
    "100022": False,
    "100023": False,
    "100024": False,
    "100025": False,
    "100026": False,
    "100027": False,
    "100028": False,
    "100029": False,
    "100030": False,
    "100031": False,
    "100032": False,
    "100033": False,
    "100034": False,
    "100035": False,
    "100036": False,
    "100037": False,
    "100038": False,
    "100039": False,
    "100040": False,
    "100041": False,
    "100042": False,
    "100043": False,
    "100044": False,
    "100045": False,
    "100046": False,
    "100047": False,
    "100048": False,
    "100049": False,
    "100050": False,
    "100051": False,
    "100052": False,
    "100053": False,
    "100054": False,
    "100055": False,
    "100056": False,
    "100057": False,
    "100058": False,
    "100059": False,
    "100060": False,
    "100061": False,
    "100062": False,
    "100063": False,
    "100064": False,
    "100065": False,
    "100066": False,
    "100067": False,
    "100068": False,
    "100069": False,
    "100070": False,
    "100071": False,
    "100072": False,
    "100073": False,
    "100074": False,
    "100075": False,
    "100076": False,
    "100077": False,
    "100078": False,
    "100079": False,
    "100080": False,
    "100081": False,
    "100082": False,
    "100083": False,
    "100084": False,
    "100085": False,
    "100086": False,
    "100087": False,
    "100088": False,
    "100089": False,
    "100090": False,
    "100091": False,
    "100092": False,
    "100093": False,
    "100094": False,
    "100095": False,
    "100096": False,
    "100097": False,
    "100098": False,
    "100099": False,
    "100100": False,
    "100101": False,
    "100102": False,
    "100103": False,
    "100104": False,
    "100105": False,
    "100106": False,
    "100107": False,
    "100108": False,
    "100109": False,
    "100110": False,
    "100111": False,
    "100112": False,
    "100113": False,
    "100114": False,
    "100115": False,
    "100116": False,
    "100117": False,
    "100118": False,
    "100119": False,
    "100120": False,
    "100121": False,
    "100122": False,
    "100123": True,
    "100124": True,
    "100125": True,
    "100126": True,
    "100127": True,
    "100128": True,
    "100129": True,
    "100130": True,
    "100131": True,
    "100132": True,
    "100133": True,
    "100134": True,
    "100135": True,
    "100136": True,
    "100137": True,
    "100138": True,
    "100139": True,
    "100140": True,
    "100141": True,
    "100142": True,
    "100143": True,
    "100144": True,
    "100145": True,
    "100146": True,
    "100147": True,
    "100148": True,
    "100149": True,
    "100150": True,
    "100151": True,
    "100152": True,
    "100153": True,
    "100154": True,
    "100155": True,
    "100156": True,
    "100157": True,
    "100158": True,
    "100159": True,
}

geo_531359170_experiance = {
    "100001": True,
    "100002": False,
    "100003": True,
    "100004": False,
    "100005": True,
    "100006": True,
    "100007": False,
    "100008": True,
    "100009": True,
    "100010": True,
    "100011": True,
    "100012": False,
    "100013": True,
    "100014": True,
    "100015": True,
    "100016": True,
    "100017": False,
    "100018": False,
    "100019": False,
    "100020": True,
    "100021": True,
    "100022": True,
    "100023": True,
    "100024": True,
    "100025": False,
    "100026": False,
    "100027": True,
    "100028": False,
    "100029": True,
    "100030": True,
    "100031": True,
    "100032": False,
    "100033": False,
    "100034": True,
    "100035": True,
    "100036": True,
    "100037": True,
    "100038": True,
    "100039": True,
    "100040": False,
    "100041": False,
    "100042": False,
    "100043": True,
    "100044": True,
    "100045": True,
    "100046": False,
    "100047": False,
    "100048": True,
    "100049": True,
    "100050": True,
    "100051": True,
    "100052": True,
    "100053": True,
    "100054": True,
    "100055": True,
    "100056": True,
    "100057": True,
    "100058": True,
    "100059": True,
    "100060": True,
    "100061": True,
    "100062": False,
    "100063": True,
    "100064": True,
    "100065": True,
    "100066": True,
    "100067": True,
    "100068": False,
    "100069": False,
    "100070": True,
    "100071": False,
    "100072": True,
    "100073": True,
    "100074": True,
    "100075": True,
    "100076": True,
    "100077": True,
    "100078": False,
    "100079": True,
    "100080": True,
    "100081": True,
    "100082": True,
    "100083": False,
    "100084": True,
    "100085": False,
    "100086": True,
    "100087": True,
    "100088": False,
    "100089": False,
    "100090": False,
    "100091": False,
    "100092": False,
    "100093": True,
    "100094": False,
    "100095": True,
    "100096": True,
    "100097": True,
    "100098": True,
    "100099": True,
    "100100": False,
    "100101": True,
    "100102": True,
    "100103": False,
    "100104": True,
    "100105": False,
    "100106": True,
    "100107": False,
    "100108": True,
    "100109": True,
    "100110": True,
    "100111": True,
    "100112": True,
    "100113": True,
    "100114": True,
    "100115": False,
    "100116": True,
    "100117": False,
    "100118": True,
    "100119": True,
    "100120": True,
    "100121": False,
    "100122": True,
    "100123": True,
    "100124": True,
    "100125": True,
    "100126": False,
    "100127": True,
    "100128": False,
    "100129": True,
    "100130": True,
    "100131": False,
    "100132": True,
    "100133": False,
    "100134": True,
    "100135": False,
    "100136": False,
    "100137": True,
    "100138": True,
    "100139": True,
    "100140": False,
    "100141": True,
    "100142": True,
    "100143": True,
    "100144": True,
    "100145": False,
    "100146": False,
    "100147": True,
    "100148": True,
    "100149": True,
    "100150": True,
    "100151": True,
    "100152": True,
    "100153": False,
    "100154": True,
    "100155": False,
    "100156": True,
    "100157": False,
    "100158": True,
    "100159": True,
}

operator_availability = {
    "100001": False,
    "100002": True,
    "100003": False,
    "100004": False,
    "100005": True,
    "100006": False,
    "100007": False,
    "100008": False,
    "100009": False,
    "100010": False,
    "100011": True,
    "100012": True,
    "100013": False,
    "100014": True,
    "100015": False,
    "100016": False,
    "100017": False,
    "100018": True,
    "100019": False,
    "100020": True,
    "100021": False,
    "100022": True,
    "100023": True,
    "100024": False,
    "100025": True,
    "100026": True,
    "100027": False,
    "100028": True,
    "100029": True,
    "100030": False,
    "100031": True,
    "100032": False,
    "100033": False,
    "100034": False,
    "100035": True,
    "100036": True,
    "100037": False,
    "100038": True,
    "100039": False,
    "100040": False,
    "100041": False,
    "100042": False,
    "100043": True,
    "100044": False,
    "100045": True,
    "100046": True,
    "100047": True,
    "100048": True,
    "100049": False,
    "100050": False,
    "100051": False,
    "100052": False,
    "100053": False,
    "100054": True,
    "100055": False,
    "100056": False,
    "100057": False,
    "100058": False,
    "100059": False,
    "100060": True,
    "100061": False,
    "100062": True,
    "100063": True,
    "100064": False,
    "100065": False,
    "100066": False,
    "100067": True,
    "100068": False,
    "100069": False,
    "100070": True,
    "100071": True,
    "100072": True,
    "100073": True,
    "100074": False,
    "100075": False,
    "100076": False,
    "100077": False,
    "100078": False,
    "100079": True,
    "100080": True,
    "100081": True,
    "100082": True,
    "100083": False,
    "100084": True,
    "100085": True,
    "100086": False,
    "100087": False,
    "100088": True,
    "100089": True,
    "100090": True,
    "100091": False,
    "100092": False,
    "100093": False,
    "100094": False,
    "100095": True,
    "100096": False,
    "100097": False,
    "100098": False,
    "100099": False,
    "100100": True,
    "100101": True,
    "100102": False,
    "100103": True,
    "100104": True,
    "100105": True,
    "100106": False,
    "100107": True,
    "100108": True,
    "100109": False,
    "100110": True,
    "100111": True,
    "100112": True,
    "100113": False,
    "100114": False,
    "100115": True,
    "100116": False,
    "100117": True,
    "100118": False,
    "100119": False,
    "100120": True,
    "100121": True,
    "100122": False,
    "100123": True,
    "100124": True,
    "100125": True,
    "100126": True,
    "100127": False,
    "100128": True,
    "100129": True,
    "100130": False,
    "100131": True,
    "100132": False,
    "100133": True,
    "100134": False,
    "100135": True,
    "100136": True,
    "100137": True,
    "100138": True,
    "100139": True,
    "100140": True,
    "100141": True,
    "100142": True,
    "100143": False,
    "100144": False,
    "100145": True,
    "100146": True,
    "100147": True,
    "100148": True,
    "100149": False,
    "100150": True,
    "100151": False,
    "100152": True,
    "100153": False,
    "100154": False,
    "100155": False,
    "100156": False,
    "100157": False,
    "100158": False,
    "100159": False,
}

n_worker_order_1 = 2
n_worker_order_2 = 4
n_worker_order_3 = 4

orders_list = [
    {
        "Order ID": 1,
        "UTE": 4,
        "Geometry": 531_359_170,
        "line": 20,
        "backup line": 24,
        "requried number of operators": 4,
        "requried number of stevedors": n_worker_order_1,
        "weight": 1.47,
        "type of part": "small parts",
        "pieces per container": 600,
        "mandatory": 0,
        "due date": 1,
        "quantity to produce": 10_000,
        "CNO": 515,  # per hour
    },
    {
        "Order ID": 2,
        "UTE": 4,
        "Geometry": 6_700_083_110,
        "line": 18,
        "backup line": 19,
        "requried number of operators": 6,
        "requried number of stevedors": n_worker_order_2,
        "weight": 12,
        "type of part": "roof",
        "pieces per container": 12,
        "mandatory": 0,
        "due date": 1,
        "quantity to produce": 5_000,
        "CNO": 91,  # per hour
    },
    {
        "Order ID": 3,
        "UTE": 4,
        "Geometry": 1_343_314_080,
        "line": 17,
        "backup line": 19,
        "requried number of operators": 6,
        "requried number of stevedors": n_worker_order_3,
        "weight": 7.7,
        "type of part": "other meddle structural parts",
        "pieces per container": 39,
        "mandatory": 1,
        "due date": 3,
        "quantity to produce": 1_000,
        "CNO": 323,  # per hour
    }
]

orders_dict = {
    "1": {
        "Order ID": 1,
        "UTE": 4,
        "Geometry": 531_359_170,
        "line": 20,
        "backup line": 24,
        "requried number of operators": 4,
        "requried number of stevedors": n_worker_order_1,
        "weight": 1.47,
        "type of part": "small parts",
        "pieces per container": 600,
        "mandatory": 0,
        "due date": 1,
        "quantity to produce": 10_000,
        "CNO": 515,  # per hour
    },
    "2": {
        "Order ID": 2,
        "UTE": 4,
        "Geometry": 6_700_083_110,
        "line": 18,
        "backup line": 19,
        "requried number of operators": 6,
        "requried number of stevedors": n_worker_order_2,
        "weight": 12,
        "type of part": "roof",
        "pieces per container": 12,
        "mandatory": 0,
        "due date": 1,
        "quantity to produce": 5_000,
        "CNO": 91,  # per hour
    },
    "3": {
        "Order ID": 3,
        "UTE": 4,
        "Geometry": 1_343_314_080,
        "line": 17,
        "backup line": 19,
        "requried number of operators": 6,
        "requried number of stevedors": n_worker_order_3,
        "weight": 7.7,
        "type of part": "other meddle structural parts",
        "pieces per container": 39,
        "mandatory": 1,
        "due date": 3,
        "quantity to produce": 1_000,
        "CNO": 323,  # per hour
    }

}

if __name__ == '__main__':
    log.info("The following code uses the OR-Tools linear solver Linear Sum Assignment Solver "
             "(https://developers.google.com/optimization/assignment/linear_assignment)")
    log.info("It's adapted to the CRF use case.")

    log.info("The hard coded data was fetched from the knowledge base on '08.11.23'")
    log.info("The data has the following shapes:")
    log.info(f"len(stevedore_suitability): {len(stevedore_suitability)}")
    log.info(f"len(UTE_4_experience): {len(UTE_4_experience)}")
    log.info(f"len(geo_531359170_experiance): {len(geo_531359170_experiance)}")
    log.info(f"len(operator_availability): {len(operator_availability)}")
    log.info(f"len(orders_list): {len(orders_list)}")
    log.info(f"len(orders_dict): {len(orders_dict)}")

    matrix_entry_example = {
        "Availability": True,
        "Medical Condition": True,
        "Experience on the UTE": True,
        "Worker resilience": 0.5,
        "Production Priority": True,
        "Due dates": 2,
        "Worker Preferences": 0.1,
        "Workers Required": 4,
    }

    log.info("This data is used to construct a matix, that can be considered the input for the solver")
    log.info("The matrix has the following shape: #workers x #orders")
    log.info(f"a cell the matrix is of type 'dict'. The following example indicates the key value pairs: "
             f"\n{pprint.pformat(matrix_entry_example)}")

    log.info("In this example code the fields 'Worker Preferences' and 'Worker resilience' will be randomised to values"
             " between 0 and 1 using the 'random.random()' function.")

    start_time_setup = time.perf_counter()
    num_orders = 3
    num_workers = 159

    # init mappings between index and id
    worker_id_to_index_mapping = {}
    worker_index_to_id_mapping = {}
    for i in range(num_workers):
        worker_id_to_index_mapping[f"{100_001 + i}"] = i
        worker_index_to_id_mapping[i] = f"{100_001 + i}"

    order_id_to_index_mapping = {
        "1": 0,
        "2": 1,
        "3": 2,
    }
    order_index_to_id_mapping = {
        0: "1",
        1: "2",
        2: "3",
    }
    log.info(f"This example uses '{num_workers}' Worker and '{num_orders}' Orders.")
    log.info(f"Order data (taken from 'WorkerloadBalance_Foundations_D4.2.xlsx' on '08.11.23'): "
             f"\n {pprint.pformat(orders_list)}")

    log.info(f"creating input matrix...")
    log.info(f"""
        'Availability' is taken from 'operator_availability'
        'Medical Condition' is taken from 'stevedore_suitability'
        'Experience on the UTE' is taken from 'stevedore_suitability'
        
        'Production Priority' is taken from 'orders_dict' (field 'mandatory') 
        'Due dates' is taken from 'orders_dict' (field 'due date') 
        
        as stated in 'Data Homogenization - Updated.docx' form (07.11.23)
    """)
    # row corresponds to a worker
    # column corresponds to an order
    # a cell is one "homogenized data" entry
    aggregated_input_data_for_the_solver = [
        [
            {
                "woker_id": worker_index_to_id_mapping[worker_index],
                "Availability": operator_availability[worker_index_to_id_mapping[worker_index]],
                "Medical Condition": stevedore_suitability[worker_index_to_id_mapping[worker_index]],
                "Experience on the UTE": stevedore_suitability[worker_index_to_id_mapping[worker_index]],
                "Worker resilience": random.random(),  # todo: JR input
                "Production Priority": orders_dict[order_index_to_id_mapping[order_index]]["mandatory"],
                "Due dates": orders_dict[order_index_to_id_mapping[order_index]]["due date"],
                "Worker Preferences": random.random(),  # todo: KB values
                "Workers Required": orders_dict[order_index_to_id_mapping[order_index]]["requried number of stevedors"],
            }
            for order_index in range(num_orders)
        ]
        for worker_index in range(num_workers)
    ]

    log.info("rows correnspont to workers and coulumns correspond to orders")
    log.info(
        f"the first row (woker '{worker_index_to_id_mapping[0]}') of the following values: \n {pprint.pformat(aggregated_input_data_for_the_solver[0])}")
    log.info(f"the matrix contains infromatrion for the workers: {pprint.pformat(worker_index_to_id_mapping.values())} "
             f"and the orders: {pprint.pformat(order_index_to_id_mapping.values())}")

    # check number of required workers
    req_workers = sum([
        order_values_dict["requried number of stevedors"] for order_values_dict in orders_dict.values()
    ])
    available_workers = sum([
        1 for bool_val in operator_availability.values() if bool_val is True
    ])

    log.info(
        f"The provided orders require: {req_workers},  the provided contains available workers: {available_workers}")
    log.info(f"available workers: {[w_id for w_id, bool_val in operator_availability.items() if bool_val is True]}")

    log.info(f"In order to use the 'ortools.graph.python.linear_sum_assignment.SimpleLinearSumAssignment()' solver"
             f" one task for every stevedore will be created."
             f" Additionally dummy tasks will be created to be assigened to not available workers and not allocated workers."
             f" This is needed to adhere to the 'SimpleLinearSumAssignment' API.")

    if available_workers < req_workers:
        log.error("Not enough available workers")
        raise Exception("Not enough available workers")

    # cost matrix has to have the #workers rows and #workers colums
    tasks = []
    task_num_to_task_str = {}
    task_details = []

    for order in orders_list:
        for stevedore in range(order["requried number of stevedors"]):
            task_num_to_task_str[len(tasks)] = f"order_{order['Order ID']}_stevedore_{stevedore}"
            tasks.append(f"order_{order['Order ID']}_stevedore_{stevedore}")
            task_details.append(
                {
                    "task": f"order_{order['Order ID']}_stevedore_{stevedore}",
                    "order_dict": order,
                    "stevedore": f"stevedore_{stevedore}",
                    "is_dummy": False,
                }
            )

    required_dummy_tasks = num_workers - req_workers
    for dummy_task in range(required_dummy_tasks):
        task_num_to_task_str[len(tasks)] = f"dummy_task_{dummy_task}"
        tasks.append(f"not_assigned_worker_{dummy_task}")
        task_details.append(
            {
                "task": f"not_assigned_worker_{dummy_task}",
                "order_dict": None,
                "stevedore": None,
                "is_dummy": True,
            }
        )

    log.info(f"tasks: {tasks[:req_workers]}")
    log.info(f"number of dummy tasks: {required_dummy_tasks} "
             f"( = {num_workers} (#wokers)- {req_workers} (#required workers) )")

    log.info("creating empty cost matrix...")
    cost_matrix = [['NA' for _ in range(num_workers)] for _ in range(num_workers)]
    log.info("populating cost matrix...")


    def cost_function(homogenized_data_dict: dict = None, order_dict: dict = None) -> float | str:
        cost_supremum = 100_000
        # handle dummy tasks
        if order_dict is None or homogenized_data_dict is None:
            return cost_supremum

        # handle exclusive constraints
        if homogenized_data_dict["Availability"] is False:
            return "NA"
        if homogenized_data_dict["Medical Condition"] is False:
            return "NA"

        # calculate cost
        # this can be any function of the homogenized data and the order data
        # make sure that cost_supremum is bigger that the biggest possible cost

        experience_cost = 1 if homogenized_data_dict["Experience on the UTE"] is True else 10
        priority_cost = 1 if homogenized_data_dict["Production Priority"] is True else 10
        due_date_cost = homogenized_data_dict["Due dates"]
        preference_cost = 1 / (homogenized_data_dict["Worker Preferences"] + 0.01)
        resilience_cost = 1 / (homogenized_data_dict["Worker resilience"] + 0.01)

        ute_cost = 0 * order_dict["UTE"]

        total_cost = 5 * preference_cost + \
                     1 * resilience_cost + \
                     1 * experience_cost + \
                     1 * priority_cost + \
                     1 * due_date_cost + ute_cost

        # upper limit for this cost formulation is
        # 1*10 + 1*10 + 1*3 (due dates) + 1*100 (resilience) 5*100 (preference) = 623 << 100_000 (cost_supremum)

        return total_cost


    # populate cost matrix
    for row, agg_row in zip(range(num_workers), aggregated_input_data_for_the_solver):
        for col, t_details in zip(range(len(tasks)), task_details):
            order_dict = t_details["order_dict"]
            if order_dict is None:
                cost_matrix[row][col] = cost_function(order_dict=None)
                continue

            o_index = order_id_to_index_mapping[f"{order_dict['Order ID']}"]
            homogenized_cell_dict = agg_row[o_index]

            cost_matrix[row][col] = cost_function(
                order_dict=order_dict,
                homogenized_data_dict=homogenized_cell_dict
            )

    end_time_setup = time.perf_counter()
    setup_data_duration = end_time_setup - start_time_setup


    start_time_solver_setup = time.perf_counter()
    assignment = linear_sum_assignment.SimpleLinearSumAssignment()

    for worker in range(0, num_workers):
        for task in range(0, num_workers):
            if cost_matrix[worker][task] != 'NA':
                assignment.add_arcs_with_cost(worker, task, cost_matrix[worker][task])

    end_time_solver_setup = time.perf_counter()

    solver_setup_duration = end_time_solver_setup - start_time_solver_setup

    start_time_solving = time.perf_counter()
    status = assignment.solve()
    end_time_solving = time.perf_counter()

    solving_duration = end_time_solving - start_time_solving

    if status == assignment.OPTIMAL:
        log.info(f"""
        
'OPTIMAL' solution found:
        
        """)
        total_cost = 0
        for i in range(0, assignment.num_nodes()):
            t_index = assignment.right_mate(i)
            t_details = task_details[t_index]
            if t_details['is_dummy']:
                continue
            order_dict = t_details['order_dict']
            order_id = order_dict['Order ID']
            order_index = order_id_to_index_mapping[f"{order_id}"]
            worker_id = worker_index_to_id_mapping[i]
            homogenized_cell_dict = aggregated_input_data_for_the_solver[i][order_index]
            total_cost += assignment.assignment_cost(i)
            log.info(
                f"Worker '{worker_id}' assigned to Order '{order_dict['Order ID']}' "
                f"(task '{assignment.right_mate(i)}', '{t_details['task']}')."
                f" Cost = {assignment.assignment_cost(i)}"
                f" Pref.: {homogenized_cell_dict['Worker Preferences']:.2f}"
                f" Resil.: {homogenized_cell_dict['Worker resilience']:.2f}"
            )
            # sanity check
            #log.info(f"{pprint.pformat(homogenized_cell_dict)}")
            if not homogenized_cell_dict["Availability"]:
                raise ValueError(f"Woker {worker_id} is not available, but was assigned to a non dummy task.")
            if operator_availability[worker_id] is False:
                raise ValueError(f"Woker {worker_id} is not available, but was assigned to a non dummy task.")

            if not homogenized_cell_dict["Medical Condition"]:
                raise ValueError(f"'Medical Condition' for Woker {worker_id} is 'False', but was assigned.")
            if stevedore_suitability[worker_id] is False:
                raise ValueError(f"'Medical Condition' for Woker {worker_id} is 'False', but was assigned.")

        log.info(f"total cost: {total_cost}")
    elif status == assignment.INFEASIBLE:
        log.error("No assignment is possible.")
    elif status == assignment.POSSIBLE_OVERFLOW:
        log.error("Some input costs are too large and may cause an integer overflow.")

    log.info(f"""Runtime information:
setup data duration (process raw data): {setup_data_duration:.4f} sec
solver setup duration (load cost matrix): {solver_setup_duration:.4f} sec
solving_duration: {solving_duration:.4f} sec
    
total duration: {setup_data_duration + solver_setup_duration + solving_duration:.2f} sec
    """)
