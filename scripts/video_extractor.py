import cv2
import os

def ekstrak_frame_video(video_path, output_dir, prefix="foto", interval_detik=1.0):
    os.makedirs(output_dir, exist_ok=True)
    cap = cv2.VideoCapture(video_path)
    
    fps = cap.get(cv2.CAP_PROP_FPS)
    if fps == 0:
        fps = 30
    frame_interval = int(fps * interval_detik)
    
    frame_id = 0
    saved_count = 0
    
    print(f"Mengekstrak dari {video_path}...")
    while cap.isOpened():
        ret, frame = cap.read()
        if not ret:
            break
            
        if frame_id % frame_interval == 0:
            # Resize jika resolusi terlalu besar (misal 4K diubah ke lebar 1280px)
            h, w = frame.shape[:2]
            if w > 1280:
                new_w = 1280
                new_h = int(h * (1280 / w))
                frame = cv2.resize(frame, (new_w, new_h), interpolation=cv2.INTER_AREA)
                
            filename = os.path.join(output_dir, f"{prefix}_{saved_count:03d}.jpg")
            cv2.imwrite(filename, frame)
            saved_count += 1
            
        frame_id += 1
        
    cap.release()
    print(f"Selesai! Berhasil mengekstrak {saved_count} foto ke folder '{output_dir}'.")

ekstrak_frame_video("scripts/mouse_2.mp4", "dataset/raw_images", prefix="gambar_mouse2", interval_detik=3.0)
# Contoh Pemakaian:
# ekstrak_frame_video("video_meja_kerja.mp4", "dataset/raw_images", prefix="meja_kerja")