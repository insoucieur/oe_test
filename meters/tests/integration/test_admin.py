def test_reading_admin(admin_client):
    response = admin_client.get("/admin/meters/reading/")
    assert response.status_code == 200
