import React from 'react'
import { Link, Routes, Route } from 'react-router-dom'
import Receipts from './pages/Receipts'
import ReceiptDetail from './pages/ReceiptDetail'
import FormsDemo from './pages/FormsDemo'

export default function App() {
  return (
    <div>
      <nav>
        <Link to="/">Receipts</Link> | <Link to="/forms">Forms Demo</Link>
      </nav>
      <Routes>
        <Route path="/" element={<Receipts />} />
        <Route path="/receipts/:id" element={<ReceiptDetail />} />
        <Route path="/forms" element={<FormsDemo />} />
      </Routes>
    </div>
  )
}