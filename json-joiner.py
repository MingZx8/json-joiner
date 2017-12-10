#!/usr/bin/env python
# -*- coding: utf-8 -*-
# @Author: MingZ
# @Date created: 11 Sep 2017
# @Date last modified: 11 Sep 2017
# Python Version: 2.7

# Build a simple joiner that accepts two files each containing an array of json objects.
# The user can specify any key that is shared in both files to join on.
# Produce a new array with the joined objects.
# For simplicity follow the conventions of a standard SQL inner join, implementing outer joins as well.
# Runtime under O(n2).
# Join the supplied customers file to the supplied orders file. Using the keys `cid` and `customer_id` respectively.

# join two json files
import json

with open('orders.json','r') as f_orders:
	orders = json.load(f_orders)
with open('customers.json','r') as f_customers:
	customers = json.load(f_customers)

cus_dict = {}
for d in customers:
	cus_dict[d['cid']] = d['name']


# inner joins
join_dict = []
for d in orders:
	for cid in cus_dict:
		if d['customer_id'] == cid:
			d['cid'] = cid
			d['name'] = cus_dict[cid]
			join_dict.append(d)
			break

# # outer joins
# join_dict = orders
# for d in join_dict:
# 	for cid in cus_dict:
# 		if d['customer_id'] == cid:
# 			d['cid'] = cid
# 			d['name'] = cus_dict[cid]
# 			break
# 		else:
# 			d['cid'] = None
# 			d['name'] = None


with open('join_json.json','w') as f_joint:
	json.dump(join_dict,f_joint,indent = 4, sort_keys=True)

#the total for orders placed by Barry and Steve#

with open('join_json.json','r') as f_joint:
	join = json.load(f_joint)

order_amount = 0
for elm in join:
	if elm['name'] == 'Barry' or elm['name'] == 'Steve':
		order_amount += elm['price']

print "total for orders places by Steve and Barry is", order_amount
