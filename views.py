from app import app, Resource, session

from flask import jsonify, request


# This route returns json object with all data from DB
@app.route('/resources', methods=['GET'])
def get_resources():
	resources = Resource.query.all()
	data = []
	for resource in resources:
		cost = resource.amount * resource.price
		data.append({
			'title': resource.title,
			'id': resource.id,
			'amount': resource.amount,
			'': resource.measurement,
			'price': resource.price,
			'cost': cost,
			'date': f'{resource.create_at.day}-{resource.create_at.month}-{resource.create_at.year}'
			})

	return jsonify({'resources': data, 'total_count': Resource.query.count()}), 200


# This route adds new resource into DB and returns it like json
@app.route('/resources', methods=['POST'])
def add_resource():
	print(request.json)
	new_resource = Resource(**request.json)
	session.add(new_resource) # add data into session
	session.commit() # add data into DB
	data = {
		'title': new_resource.title,
		'amount': new_resource.amount,
		'': new_resource.measurement,
		'price': new_resource.price,
		'date': request.json['create_at']
	}

	return jsonify(data), 201 # jsonify turns data to json 


# This route changes one record 
@app.route('/resources/<int:resources_id>', methods=['PUT'])
def update_resource(resources_id):
	item = Resource.query.filter(Resource.id == resources_id).first()
	params = request.json
	if not item:
		return {'message': 'No resource with this id'}, 400
	for key, value in params.items():
		setattr(item, key, value)
	session.commit()
	data = {
		'title': item.title,
		'id': item.id,
		'amount': item.amount,
		'price': item.price,
		'date': request.json['create_at']
	}

	return data, 201


# This route deletes one record from DB
@app.route('/resources/<int:resources_id>', methods=['DELETE'])
def delete_resources(resources_id):
	item = Resource.query.filter(Resource.id == resources_id).first()
	if not item:
		return {'message': 'No resource with this id'}, 400
	session.delete(item)
	session.commit()

	return '', 204


# This route returns total cost of all records
@app.route('/total_cost', methods=['GET'])
def get_total_cost():
	total_cost = 0
	resources = Resource.query.all()
	for resource in resources:
		total_cost += resource.amount * resource.price

	return {'total_cost': total_cost}, 200
