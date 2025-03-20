import Table from '@mui/material/Table';
import TableBody from '@mui/material/TableBody';
import TableCell from '@mui/material/TableCell';
import TableContainer from '@mui/material/TableContainer';
import TableHead from '@mui/material/TableHead';
import TableRow from '@mui/material/TableRow';
import Typography from '@mui/material/Typography';
import Paper from '@mui/material/Paper';
import React, { useEffect, useState } from 'react';
import { apiGetRequest } from './API';

function createData(id, provider, npi, client, date, time, status) {
    return { id ,provider, npi, client, date, time, status};
}

// delete this later
const rows = [
    createData(1, 'Larissa Zhang', 1234567890, "Client 1", "2025-03-19", "10:58:06", "booked"),
    createData(2, 'David Jones', 1234567890,'Client 2', "2025-03-19", "10:58:06", "booked"),
];

export default function AppTable() {
    const [appointments, setAppointments] = useState([]);

    useEffect(() => {
        apiGetRequest('/api/appointments/')
            .then((data) => {
                setAppointments(data.appointments);
                console.log(data);
            })
            .catch((error) => {
                console.log(error.message);
            });
    }, []);
    
    return (
        <TableContainer component={Paper}>
            <Typography
                variant="h5"
                component="div"
            >
                Appointments
            </Typography>
            <Table sx={{ minWidth: 900 }} aria-label="simple table">
                <TableHead>
                    <TableRow>
                        <TableCell>Provider</TableCell>
                        <TableCell>Provider NPI</TableCell>
                        <TableCell>Client</TableCell>
                        <TableCell>Date</TableCell>
                        <TableCell>Appointment Time</TableCell>
                        <TableCell>Status</TableCell>
                    </TableRow>
                </TableHead>
                <TableBody>
                    {rows.map((row) => (
                        // delete this temp information later
                        <TableRow key={row.id}>
                            <TableCell>{row.provider}</TableCell>
                            <TableCell>{row.npi}</TableCell>
                            <TableCell>{row.client}</TableCell>
                            <TableCell>{row.date}</TableCell>
                            <TableCell>{row.time}</TableCell>
                            <TableCell>{row.status}</TableCell>
                        </TableRow>
                    ))}

                    {appointments.map((appointment) => {
                        const providerName = appointment.provider.first_name + " " + appointment.provider.last_name;
                        const clientName = appointment.client.first_name + " " + appointment.client.last_name;
                        return (
                            <TableRow key={appointment.id}>
                            <TableCell>{providerName}</TableCell>
                            <TableCell>{appointment.provider.npi}</TableCell>
                            <TableCell>{clientName}</TableCell>
                            <TableCell>{appointment.date}</TableCell>
                            <TableCell>{appointment.time}</TableCell>
                            <TableCell>{appointment.status}</TableCell>
                            </TableRow>
                        );
                    }

                    )}
                </TableBody>
            </Table>
        </TableContainer>
    );
}