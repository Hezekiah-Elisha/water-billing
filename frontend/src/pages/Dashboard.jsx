import React from 'react'
import SideNav from '../components/SideNav'
import { Routes, Route } from 'react-router-dom'
import DashHome from './DashHome'
import DashZones from './DashZones'
import DashSupervisors from './DashSupervisors'
import DashWorkers from './DashWorkers'
import DashBills from './DashBills'
import DashMeters from './DashMeters'
import DashMeterReadings from './DashMeterReadings'
import DashCustomers from './DashCustomers'
import DashNotifications from './DashNotifications'
import DashProfile from './DashProfile'
import DashSettings from './DashSettings'
import PrivateRoute from '../components/PrivateRoute'


export default function Dashboard() {
    return (
    <div className='flex flex-row'>
        <SideNav />
        
        <div className="flex-1 p-10">

            <Routes>
                <Route path='' element={ <DashHome/> } />
                <Route path='home' element={ <DashHome/> } />
                <Route path='zones' element={ <DashZones/> } />
                <Route path='supervisors' element={ <DashSupervisors/> } />
                <Route path='workers' element={ <DashWorkers/> } />
                <Route path='bills' element={ <DashBills/> } />
                <Route path='meters' element={ <DashMeters/> } />
                <Route path='meter-readings' element={ <DashMeterReadings/> } />
                <Route path='customers' element={ <DashCustomers/> } />
                <Route path='notifications' element={ <DashNotifications/> } />
                <Route element={ <PrivateRoute/> }>
                    <Route path='profile' element={ <DashProfile/> } />
                </Route>
                <Route path='settings' element={ <DashSettings/> } />
            </Routes>
            
                
        </div>
    </div>
  )
}
