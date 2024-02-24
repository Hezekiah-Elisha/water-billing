import { useState, useEffect } from 'react'
import api from '../api'
import { PhoneIcon } from '@heroicons/react/24/solid'

export default function DashCustomers() {
  const [customers, setCustomers] = useState([])
  const [loading, setLoading] = useState(false)
  const [error, setError] = useState(null)

  const [zones, setZones] = useState({});
  const [ meters, setMeters ] = useState({});

  useEffect(() => {
    const fetchMeters = async () => {
      try {
        const response = await api.get('/meters');
        setMeters(response.data.reduce((info, meter) => ({ ...info, [meter.id]: meter.meter_number }), {}));
      } catch (error) {
        console.error(error);
      }
    };
    fetchMeters();
  }, []);

  useEffect(() => {
    const fetchZones = async () => {
      try {
        const response = await api.get('/zones');
        setZones(response.data.reduce((acc, zone) => ({ ...acc, [zone.id]: zone.name }), {}));
      } catch (error) {
        console.error(error);
      }
    };
    fetchZones();
  }, []);


  useEffect(() => {
    const fetchCustomers = async () => {
      try {
        setLoading(true)
        const response = await api.get('/customers')
        setCustomers(response.data)
        setLoading(false)
      } catch (error) {
        setError(error)
      }
    }
    fetchCustomers()
    }, []
  )

  if (loading) return <div>Loading...</div>
  if (error) return <div>{error.message}</div>

  return (
    <div>
      <h1 className='font-bold text-2xl'>Customers</h1>
      <hr />
      <div className='grid grid-cols-4 gap-4'>
        {customers.map((customer, index) => (
          <div key={index} className="max-w-sm rounded overflow-hidden shadow-lg">
            <div className="px-6 py-4">
              <div className="font-bold text-xl mb-2 capitalize">{customer.name}</div>
              <p className="text-gray-700 text-base flex flex-row">
                <PhoneIcon className="h-4 w-4"/>{customer.phone_number}
              </p>
            </div>
            <div className="px-6 pt-4 pb-2">
              <span className="inline-block bg-gray-200 rounded-full px-3 py-1 text-sm font-semibold text-gray-700 mr-2 mb-2">{customer.email}</span>
              <span className="inline-block bg-gray-200 rounded-full px-3 py-1 text-sm font-semibold text-gray-700 mr-2 mb-2">{meters[customer.meter_id]}</span>
              <span className="inline-block bg-gray-200 rounded-full px-3 py-1 text-sm font-semibold text-gray-700 mr-2 mb-2">Zone #{zones[customer.zone_id]}</span>
            </div>
          </div>
        ))}
      </div>
    </div>
  )
}
