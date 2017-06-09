## processing manifests from different logistics companies

def hermes_map_event(event_name):
    delivery = ['Delivery To Safe Place', 'Delivered			','Unmanifested Delivery To Safe Place', 'Unmanifested Delivered			', 'Delivered']
    collection = ['Pickup','Collection', 'Pickup From Safe Place','Unmanifested Collection','Unmanifested Pickup','Unmanifested Pickup From Safe Place']
    carried_forward = ['Delivery EOD Carry Forward', 'Pickup EOD Carry Forward','Unmanifested Delivery EOD Carry Forward','Unmanifested Pickup EOD Carry Forward']
    failed = ['Pickup Failed', 'Delivery Failed','Unmanifested Delivery Failed','Unmanifested Pickup Failed']
    missing = ['Receipt Scan Missing Parcel']
    if event_name in delivery:
        event_name = 'Delivered'
    elif event_name in collection:
        event_name = 'Collection'
    elif event_name in carried_forward:
        event_name = 'Carried Forward'
    elif event_name in failed:
        event_name = 'Failed'
    elif event_name in missing:
        event_name = 'Missing'
    return event_name
