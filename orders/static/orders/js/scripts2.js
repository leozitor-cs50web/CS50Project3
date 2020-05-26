    //control badge status for admin
    let statusBadge = document.querySelector('.statusBadge')
    let status = statusBadge.id
    if (status === 'initiated')
        statusBadge.className = "btn btn-primary statusBadge mb-3"
    else if (status === "pending")
        statusBadge.className = "btn btn-warning statusBadge mb-3"
    else if (status === 'completed')
        statusBadge.className = "btn btn-success statusBadge mb-3"
