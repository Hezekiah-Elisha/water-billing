import React from 'react'
import api from '../api'

export default function DashZones() {
    const [zones, setZones] = React.useState([])
    const [loading, setLoading] = React.useState(false)
    const [error, setError] = React.useState(null)

    React.useEffect(() => {
        const fetchZones = async () => {
            try {
                setLoading(true)
                const response = await api.get('/zones')
                setZones(response.data)
                setLoading(false)
            } catch (error) {
                setError(error)
            }
        }
        fetchZones()
    }, [])
    if (loading) return <div>Loading...</div>
    if (error) return <div>{error.message}</div>


  return (
        <div>
      <h1 className='font-bold text-2xl'>Available Zones</h1>
      <hr />
      <table className='table-auto w-full rounded'>
        <thead className='border-b'>
          <tr>
            <th className='border px-4 py-2'>Name</th>
            <th className='border px-4 py-2'>Role</th>
            <th className='border px-4 py-2'>Action</th>
          </tr>
        </thead>
        <tbody>
          {zones.map((zone, index) => (
            <tr key={index}>
              <td className='border px-4 py-2'>{zone.name}</td>
              <td className='border px-4 py-2'>{zone.description}</td>
              <td className='flex border px-4 py-2 gap-4'>
                <button className='bg-blue-500 hover:bg-blue-400 text-white font-bold py-2 px-4 rounded-full'>
                  View
                </button>
                <button className='bg-red-400 hover:bg-red-500 text-white font-bold py-2 px-4 rounded-full'>
                  Delete
                </button>
              </td>
            </tr>
          ))}
        </tbody>

      </table>
    </div>
  )
}
