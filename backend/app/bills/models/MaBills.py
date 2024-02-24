from app import db, ma
from .Bill import Bill
from marshmallow import fields, validate


class MaBills(ma.Schema):
    class Meta:
        model = Bill
        fields = ('id', 'meter_id', 'units', 'amount','status', 'created_at')

        _links = ma.Hyperlinks({
            'self': ma.URLFor('bill_details', values=dict(id='<id>')),
            'collection': ma.URLFor('bills')
        })


ma_bill = MaBills()
ma_bills = MaBills(many=True)