import React from 'react'
import { BrowserRouter, Routes, Route } from 'react-router-dom'
import Header from './components/Header'
import Home from './pages/Home'
import About from './pages/About'
import Signin from './pages/Signin'
import NotFound from './pages/NotFound'
import Dashboard from './pages/Dashboard'
import DashProfile from './pages/DashProfile'
import PrivateRoute from './components/PrivateRoute'

export default function App() {
  return (
    <BrowserRouter>
      <Header />
      <Routes>
        <Route path='/' element={ <Home/> } />
        <Route path='/about' element={ <About/> } />
        <Route path='*' element={ <NotFound/> } />
        <Route path='/signin' element={ <Signin/> } />
        <Route element={ <PrivateRoute/> }>
          <Route path='/dashboard' element={ <Dashboard/> } />
          <Route path='/dashboard/*' element={ <Dashboard/> } />
        </Route>
      </Routes>
    </BrowserRouter>
  )
}
