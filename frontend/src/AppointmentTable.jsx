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
import { Box, Button, TextField } from '@mui/material';

// creates the appointment table component
export default function AppTable() {
    const [appointments, setAppointments] = useState([]);
    const [originalApps, setOriginal] = useState([]);

    // fetch appointment data from API and populate the table rows below
    useEffect(() => {
        apiGetRequest('/api/appointments/')
        .then((data) => {
            // save two copies, one set for display/filters and the other the original data
            setAppointments(data.appointments);
            setOriginal(data.appointments);
            console.log(data);
        })
        .catch((error) => {
            console.log(error.message);
        });
    }, []);

    // filter appointments based on dates given
    const handleTimeFilter = (event) => {
        event.preventDefault();
        const data = new FormData(event.currentTarget);
        const firstDate = new Date(data.get("first_date")+"T00:00:00");
        const secondDate = new Date(data.get("last_date")+"T00:00:00");
        let newApps = appointments.slice();
        for (let i = 0; i < newApps.length; i++) {
            const val = new Date(newApps[i].date);
            if (val < firstDate || val > secondDate) {
                newApps.splice(i, 1);
            }
        }
        setAppointments(newApps);
    }

    // reset the filter with original data
    const handleResetFilter = (event) => {
        event.preventDefault();
        setAppointments(originalApps);
    }
    
    return (        
        <TableContainer component={Paper}>
            {/* Title of Table */}
            <div className='italic text-sky-600'>
               <Typography
                    variant="h5"
                    component="div"
                >
                    Appointments
                </Typography> 
            </div>
            {/* Table itself */}
            <Table sx={{ minWidth: 900 }}>
                <TableHead>
                    <TableRow 
                        sx={{textDecoration: 'underline'}}
                    >
                        <TableCell>Provider</TableCell>
                        <TableCell>Provider NPI</TableCell>
                        <TableCell>Client</TableCell>
                        <TableCell>Date</TableCell>
                        <TableCell>Appointment Time</TableCell>
                        <TableCell>Status</TableCell>
                    </TableRow>
                </TableHead>
                <TableBody>
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

            {/* Set up for the Time Filter */}
            <div className='text-sky-600'>
                <Typography
                    variant="h8"
                    component="div"
                >
                    Time Range Filter
                </Typography>
            </div>
            
            <Box
                component="form"
                onSubmit={handleTimeFilter}
                noValidate
            >
                <TextField
                    margin="normal"
                    required
                    id="first_date"
                    label="From Date (YYYY-MM-DD)"
                    name="first_date"
                    autoComplete="From Date"
                    autoFocus
                />
                <TextField
                    margin="normal"
                    required
                    id="last_date"
                    label="To Date (YYYY-MM-DD)"
                    name="last_date"
                    autoComplete="To Date"
                    autoFocus
                />
                <Button variant='contained' type='submit' sx={{ mt: 3, mb: 2 }}>
                    Filter
                </Button>
            </Box>

            <Box
                component="form"
                onSubmit={handleResetFilter}
                noValidate
            >
                <Button variant='contained' type='submit' sx={{ mt: 3, mb: 2 }}>
                    Reset
                </Button>   
            </Box>
        </TableContainer>
    );
}